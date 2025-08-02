class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        """
        BFS from buildings not lands
        assumption is there are fewer buildings than lands

        For each building:
        - BFS traversal to get distance to all reachable lands
        - +1 for number of buildings reachable by each land

        Retun min distance for land reachable by all buildings

        Time: O(B * R * C), B number of buildings, R rows, C cols
        Space: O(R * C)
        """
        rows = len(grid)
        cols = len(grid[0])
                
        dists = [[0] * cols for _ in range(rows)] #  distance from all buildings to loc
        can_reach = [[0] * cols for _ in range(rows)] # number of buildings loc can reach

        def bfs(row, col):
            q = collections.deque([(row, col, 0)])
            seen = set()
            seen.add((row, col))
            while q:
                r, c, d = q.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and grid[nr][nc] == 0:
                        can_reach[nr][nc] += 1 # loc is reachable by building
                        dists[nr][nc] += d + 1
                        seen.add((nr, nc))
                        q.append((nr, nc, d+1)) # loc has d + 1 distance from building
                        
        buildings = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    buildings += 1
                    bfs(row, col) # traverse from every building             

        min_dist = float('inf')
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and can_reach[r][c] == buildings:
                    min_dist = min(min_dist, dists[r][c])
        
        return min_dist if min_dist != float('inf') else -1

