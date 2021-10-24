class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        BFS
        
        Time O(N^2): number of nodes in our graph. 
        
        Space
        If we use visited set, space complexity is also O(N^2). 
        
        """
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]: # start/end point invalid
            return -1
        seen = set()
        q = collections.deque([(0, 0, 1)]) # i, j, step
        seen.add((0,0))
        while q:
            i, j, step = q.popleft()
            if i == n - 1 and j == n - 1: # reached goal
                return step
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1), (-1,-1), (1,1), (1,-1), (-1,1)]: 
                x = i + dx
                y = j + dy
                if 0 <= x < n and 0 <= y < n and (x,y) not in seen and grid[x][y] == 0:
                    seen.add((x, y))
                    q.append((x, y, step+1))
        return -1
