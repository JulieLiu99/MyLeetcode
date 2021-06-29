class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        """
        DP in place
        
        Time O(n)
        Space O(1)
        
        """
        
        # first column, can only go down
        for row in range(1, len(grid)):
            grid[row][0] += grid[row-1][0]
            
        # first row, can only go right
        for col in range(1, len(grid[0])):
            grid[0][col] += grid[0][col-1]
            
        # middle part, either down or right
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                
        return grid[-1][-1]
