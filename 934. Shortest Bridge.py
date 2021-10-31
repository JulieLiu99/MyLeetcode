class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        zeros = set()
        
        def dfs(i, j): # DFS on first island and find sorrounding zeros
            grid[i][j] = -1 # mark as seen
            for x, y in (i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j):
                if 0 <= x < rows and 0 <= y < cols:
                    if grid[x][y] == 1:
                        dfs(x, y)
                    if grid[x][y] == 0:
                        zeros.add((0, i, j))
                        
        def find_first_land():
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1:
                        return i, j
                    
        start_i, start_j = find_first_land()
        dfs(start_i, start_j)
        q = deque(list(zeros)) # BFS, expand the first island until it connects to the second
        while q:
            step, i, j = q.popleft()
            for x, y in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                if 0 <= x < rows and 0 <= y < cols:
                    if grid[x][y] == 1:
                        return step
                    elif grid[x][y] == 0:
                        grid[x][y] = -1  # mark as seen
                        q.append((step + 1, x, y))
