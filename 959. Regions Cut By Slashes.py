class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        """
        DP, DFS
        
        matrix[i][j][k]
        
        k: the triangle within each square cell. 
        A square cell at (i, j) contains 4 triangles (top, right, down, left).  
        ---------
        | \ 0 / | 
        |3  X  1|
        | / 2 \ |
        ---------
        
        False means not traveled to from previous cells -> a new region
        True means being cleared from previous cell visits
        
        At each triangle visit, check the cell content.
        Mark all neighbour triangles that are cleared True.
        Move on to neighbors it can travel to without barrier, without incrementing cnt.
        
        If end of unblocked visit, go back to for loop and cnt += 1.
        
        """
        
        def dfs(i, j, k):
            if 0 <= i < n > j >= 0 and not matrix[i][j][k]:

                if grid[i][j] == "*": # \
                    if k <= 1:      # top and right
                        matrix[i][j][0] = matrix[i][j][1] = True
                        dfs(i - 1, j, 2)
                        dfs(i, j + 1, 3)
                    else:   
                        matrix[i][j][2] = matrix[i][j][3] = True
                        dfs(i + 1, j, 0)
                        dfs(i, j - 1, 1)
                        
                elif grid[i][j] == "/":
                    if 1 <= k <= 2: # bottom and right
                        matrix[i][j][1] = matrix[i][j][2] = True
                        dfs(i, j + 1, 3)
                        dfs(i + 1, j, 0)
                    else:
                        matrix[i][j][0] = matrix[i][j][3] = True
                        dfs(i - 1, j, 2)
                        dfs(i, j - 1, 1)
                        
                else: # not slash
                    matrix[i][j][0] = matrix[i][j][1] = matrix[i][j][2] = matrix[i][j][3] = True
                    dfs(i - 1, j, 2)
                    dfs(i, j + 1, 3)
                    dfs(i + 1, j, 0)
                    dfs(i, j - 1, 1)
                
        # Firstly, modify grid list, changing "\" to "*" for simplicity for reading grid[i][j].
        grid = [row.replace("\\", "*") for row in grid]
        
        n = len(grid)
        
        # Make matrix array marking [top, right, down, left] of each square to zero.
        matrix = [[[False, False, False, False] for j in range(n)] for i in range(n)]
        cnt = 0
        
        for i in range(n):
            for j in range(n):
                for k in range(4):
                    # Iterate over matrix and process (dfs) if current region of the unit square is zero.
                    if not matrix[i][j][k]:
                        # Increase group number (cnt) by one before processing
                        cnt += 1
                        dfs(i, j, k)
                    
        return cnt
