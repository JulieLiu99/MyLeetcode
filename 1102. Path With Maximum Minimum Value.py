class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        """
        BFS + Heap
        
        Time O(mn log mn)
        Space O(mn)
        
        """
        rows = len(grid)
        cols = len(grid[0])
        
        heap = [(-grid[0][0], 0, 0)] # heap top is the max of "mins on each path"
        seen = [[0 for _ in range(cols)] for _ in range(rows)]
        while heap:
            val, x, y = heapq.heappop(heap) # take the max step
            if x == rows - 1 and y == cols - 1: 
                return -val
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not seen[nx][ny]:
                    seen[nx][ny] = 1 
                    heapq.heappush(heap, (max(val, -grid[nx][ny]), nx, ny)) # storing min on each path
        return -1
