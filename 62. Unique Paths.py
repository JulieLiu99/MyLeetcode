class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        """
        Recursion
        
        Time Limit Exceeded
        
        """
        
#         def find(x, y):
#             if x == n-1 and y == m-1:
#                 return 1
#             if x > n-1 or y > m-1:
#                 return 0
#             return find(x+1, y) + find(x, y+1)
         
#         return find(0, 0)   

        """
        DP
        
        Time O(mn)
        Space O(mn)
        
        """
        if not m or not n:
            return 0
        
        dp = [[1 for _ in range(n)] for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[-1][-1]
