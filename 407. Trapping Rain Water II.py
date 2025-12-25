import heapq

class Solution:
    """
    BFS + Priority Queue

    Treat edges of the grid as the initial boundary 
    Repeatedly pop the lowest boundary cell
    Move inward (check its unvisited neighbors):
    - If lower, water is trapped
    - If higher, update boundary

    Time O(mn x logmn): each heap operation costs O(log length-of-heap)
    Space O(mn)
    """
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or len(heightMap) < 3 or len(heightMap[0]) < 3:
            return 0

        rows, cols = len(heightMap), len(heightMap[0])
        visited = [[False] * cols for _ in range(rows)]
        heap = [] # (height, row, col)

        for row in range(rows):
            heapq.heappush(heap, (heightMap[row][0], row, 0))
            heapq.heappush(heap, (heightMap[row][cols-1], row, cols-1))
            visited[row][0] = visited[row][cols-1] = True
        for col in range(cols):
            heapq.heappush(heap, (heightMap[0][col], 0, col))
            heapq.heappush(heap, (heightMap[rows-1][col], rows-1, col))
            visited[0][col] = visited[rows-1][col] = True

        result = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while heap:
            height, row, col = heapq.heappop(heap)
            for d_row, d_col in directions:
                n_row, n_col = row + d_row, col + d_col
                if 0 <= n_row < rows and 0 <= n_col < cols and not visited[n_row][n_col]:
                    result += max(height - heightMap[n_row][n_col], 0)
                    valid_boundary_height = max(heightMap[n_row][n_col], height)
                    heapq.heappush(heap, (valid_boundary_height, n_row, n_col))
                    visited[n_row][n_col] = True

        return result
