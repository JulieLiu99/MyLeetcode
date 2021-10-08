class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        """
        Find shortest path -> BFS
        
        Time: O(m*n*k)
        Space: O(m*n*k)
        
        """
        
        m, n = len(grid), len(grid[0])
        q = deque([(0, 0, k)])  
        seen = set([(0, 0, k)])
        
        step = 0
        while q:
            for _ in range(len(q)):
                r, c, k = q.popleft()
                
                if r == m - 1 and c == n - 1: # reached the goal
                    return step  
                
                for nr, nc in [(r-1,c), (r,c+1), (r+1, c), (r, c-1)]:
                    if nr < 0 or nr == m or nc < 0 or nc == n: # out of bound 
                        continue  
                    nk = k - grid[nr][nc]
                    if nk >= 0 and (nr, nc, nk) not in seen:
                        seen.add((nr, nc, nk))
                        q.append((nr, nc, nk))
            step += 1

        return -1
