class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        DFS
        
        Time O(mn): we visit each edge in our graph only once. 
        Space O(mn)
        
        """
        m, n = len(grid), len(grid[0])
        islands = collections.defaultdict(int)
        color = 0
        
        def dfs(color, i, j):
            if not 0<=i<m or not 0<=j<n or grid[i][j] != 1: 
                return
            islands[color] += 1
            grid[i][j] = '#' # visited
            for x, y in [(1,0),(-1,0),(0,-1),(0,1)]: 
                dfs(color, x+i, y+j)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(color, i, j)
                    color += 1

        if not islands: 
            return 0
        else:
            return max(islands.values())

        """
        BFS

        """
#         m, n = len(grid), len(grid[0])
        
#         def bfs(r, c):
#             q = deque([(r, c)])
#             grid[r][c] = '#' # visited
#             island_area = 0
#             while q:
#                 r, c = q.popleft()
#                 island_area += 1
#                 for x, y in [(1,0),(-1,0),(0,-1),(0,1)]: 
#                     nr, nc = r + x, c + y
#                     if nr >= 0 and nr < m and nc >= 0 and nc != n and grid[nr][nc] != 0 and grid[nr][nc] != '#': 
#                         grid[nr][nc] = '#' # visited
#                         q.append((nr, nc))
#             return island_area
        
#         res = 0
#         for r in range(m):
#             for c in range(n):
#                 if grid[r][c] == 1:
#                     res = max(res, bfs(r, c))
#         return res