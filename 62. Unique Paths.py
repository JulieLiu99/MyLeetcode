class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        """
        DP
        
        Time O(mn)
        Space O(mn)
        
        """
#         if not m or not n:
#             return 0
        
#         dp = [[1 for _ in range(n)] for _ in range(m)]
        
#         for i in range(1, m):
#             for j in range(1, n):
#                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
#         return dp[-1][-1]


        """
        DP
        dp[(i, j)] = dp[(i-1, j)] + dp[(i, j-1)]
        We can get to (i, j) either from paths to (i-1, j) OR from paths to (i, j-1)
        
        Time O(m * n)
        Space O(n)
        
        """
    
        if not m or not n: return 0
        
        dp = [1] * n # a row 
        
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j-1]
                
        return dp[-1]


