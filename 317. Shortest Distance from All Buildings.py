class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        """
        BFS 
        
        0: empty land that you can pass by freely
        1: building that you cannot pass through
        2: obstacle that you cannot pass through
        
        -> build a house on an empty land that reaches all buildings in the shortest total travel distance
        
        BFS from buildings, keep counts of distances, record 0 locations accessable by every building on the board. Return the location with the min dist which can reach buildings.
        
        Time O(B * R * C)
        Space O(R * C)
        
        """
        rows = len(grid)
        cols = len(grid[0])
        
        if rows == cols == 1: return -1 # no place to build new building
        
        dists = [[0] * cols for _ in range(rows)]
        can_reach = [[0] * cols for _ in range(rows)]

        def bfs(row, col):
            q = collections.deque([(row, col, 0)])
            seen = set()
            seen.add((row, col))
            while q:
                r, c, d = q.popleft()
                for y, x in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr = r + y
                    nc = c + x
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and grid[nr][nc] == 0:
                        can_reach[nr][nc] += 1 # space can reach this building
                        dists[nr][nc] += d + 1
                        seen.add((nr, nc))
                        q.append((nr, nc, d+1)) # new loc has d + 1 distance from building
                        
        buildings = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1: # from every building
                    bfs(row, col)       
                    buildings += 1               

        min_dist = float('inf')
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and can_reach[r][c] == buildings:
                    min_dist = min(min_dist, dists[r][c])
        
        return min_dist if min_dist != float('inf') else -1

