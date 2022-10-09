class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        """
        DFS, store paths in hashset
        
        Because we always start from top right corner of island, 
        if islands have the same shape,
        their search paths should be the same!
        
        Time: O(m*n) 
        Space: O(m*n)
        
        
        [[1,0],
         [0,1]]
        
        Each island is 's du ud rl lr'
        
        [[1,0],
         [1,0],
         [0,1]]
        
        Top island is 's d du ud rl lr u ud rl lr'
                         ^             ^
        """
        islands = set([])
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(i, j, path):
            if not (0 <= i < rows and 0 <= j < cols) or grid[i][j] != 1:
                return path # out of bound, stop search
            grid[i][j] = "#" # mark as visited
            return path + dfs(i+1, j, "d") + "u" + dfs(i-1, j, "u") + "d" + dfs(i, j+1, "r") + "l" + dfs(i, j-1, "l") + "r" # try a direction and reset

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    islands.add(dfs(i, j, "s"))

        return len(islands)