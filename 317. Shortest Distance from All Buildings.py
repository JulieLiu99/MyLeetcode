class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        """
        BFS 
        
        0: empty land that you can pass by freely
        1: building that you cannot pass through
        2: obstacle that you cannot pass through
        
        -> build a house on an empty land that reaches all buildings in the shortest total travel distance
        
        BFS from buildings, keep counts of distances, record 0 locations accessable by every building on the board. Return the location with the min dist which can reach buildings.
        
        Time O(n^2)
        Space O(n)
        
        """
        rows = len(grid)
        cols = len(grid[0])
        
        if rows == cols == 1: return -1 # no place to build new building
        
        dists = collections.defaultdict(int) # loc of empty spot: distance to all buildings it can reach
        can_reach = collections.defaultdict(int)
        def bfs(row, col):
            q = collections.deque([(row, col, 0)])
            seen = set()
            while q:
                r, c, d = q.popleft()
                dists[(r, c)] += d
                for y, x in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr = r + y
                    nc = c + x
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and grid[nr][nc] == 0:
                        can_reach[(nr, nc)] += 1 # space can reach this building
                        seen.add((nr, nc))
                        q.append((nr, nc, d+1)) # new loc has d + 1 distance from building
                        
        buildings = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1: # from every building
                    bfs(row, col)       
                    buildings += 1               

        min_dist = float('inf')
        for k in dists.keys():
            if can_reach[k] == buildings:
                min_dist = min(min_dist, dists[k])
        
        return min_dist if min_dist != float('inf') else -1

        """
        BFS from every empty spot
        ^ Useful if we grid is mostly taken
        
        Correct but TLE
        
        """
#         rows = len(grid)
#         cols = len(grid[0])
        
#         if rows == cols == 1: return -1 # no place to build new building
        
#         dists = collections.defaultdict(int) # loc of empty spot: distance to all buildings it can reach
#         can_reach = collections.defaultdict(int)
#         def bfs(row, col):
#             q = collections.deque([(row, col, 0)])
#             seen = set()
#             while q:
#                 r, c, d = q.popleft()
#                 for y, x in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                     nr = r + y
#                     nc = c + x
#                     if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen:
#                         seen.add((nr, nc))
#                         if grid[nr][nc] == 0:
#                             q.append((nr, nc, d+1)) # new loc has d + 1 distance from starting point
#                         elif grid[nr][nc] == 1:
#                             dists[(row, col)] += d+1
#                             can_reach[(row, col)] += 1 # space can reach this building
                        
#         buildings = 0
#         for row in range(rows):
#             for col in range(cols):
#                 if grid[row][col] == 0: # from every space
#                     bfs(row, col) 
#                 elif grid[row][col] == 1:
#                     buildings += 1               

#         min_dist = float('inf')
#         for k in dists.keys():
#             if can_reach[k] == buildings:
#                 min_dist = min(min_dist, dists[k])
        
#         return min_dist if min_dist != float('inf') else -1

