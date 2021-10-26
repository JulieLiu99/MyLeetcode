class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        """
        find median for x coordinates, and median for y coordinates
        
        how to find medians: use two loops to get coordinates and they will be in order naturally.
        
        Time O(mn)
        Space O(m+n)
        
        """
        if not grid: return 0
        
        m = len(grid)
        n = len(grid[0])
        
        row_idx = [i for i in range(m) for j in range(n) if grid[i][j]] # horizonal first
        cow_idx = [j for j in range(n) for i in range(m) if grid[i][j]] # vertival first
        
        median_r = row_idx[len(row_idx) // 2]
        median_c = cow_idx[len(cow_idx) // 2]
        
        return sum(abs(r - median_r) for r in row_idx) + sum(abs(c - median_c) for c in cow_idx)
