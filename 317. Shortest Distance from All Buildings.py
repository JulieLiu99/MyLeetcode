class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        """
        BFS 
        
        0: empty land that you can pass by freely
        1: building that you cannot pass through
        2: obstacle that you cannot pass through
        
        -> build a house on an empty land that reaches all buildings in the shortest total travel distance
        
        BFS from buildings, keep counts of distances, record 0 locations accessable by every building on the board. Return the location with the min dist which can reach buildings.
        
        Time O(n)
        Space O(n)
        
        """
        rows = len(grid)
        cols = len(grid[0])
        
        dists = collections.defaultdict(int)
        can_reach = collections.defaultdict(set)
        
        def bfs(row, col):
            q = collections.deque([])
            q.append((row, col, 0))
            seen = set()
            seen.add((row, col))
            while q:
                r, c, d = q.popleft()
                dists[(r, c)] += d
                for y, x in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr = r + y
                    nc = c + x
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and grid[nr][nc] == 0:
                        can_reach[(nr, nc)].add((row, col)) # space can reach building
                        seen.add((nr, nc))
                        q.append((nr, nc, d+1)) # new loc has d + 1 distance from building
                        
        buildings = set()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    bfs(row, col)
                    buildings.add((row, col))
                    dists[(row, col)] = float('inf')
                    

        min_dist = float('inf')
        for k in dists:
            if dists[k] < min_dist and len(can_reach[k]) == len(buildings):
                min_dist = dists[k]
        
        return min_dist if min_dist != float('inf') else -1


