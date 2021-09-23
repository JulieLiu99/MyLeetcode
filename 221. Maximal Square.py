class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        
        DP[r+1][c+1] = max side of square with matrix[r][c] as bottom right
        DP 0th row and 0th col are for padding
        
        Time O(n^2)
        Space O(n^2)
        
        """
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        
        dp = [[0]*(cols+1) for _ in range(rows+1)]
        max_side = 0
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1 # Be careful of the indexing since dp grid has additional row and column
                    max_side = max(max_side, dp[r+1][c+1])
                
        return max_side * max_side
