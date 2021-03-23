class Solution:
    def getMoneyAmount(self, n: int) -> int:
        
        
        """
        Top down
        Recursion + Memorization
        Slower because of resursion stack
        
        Time O(n^3)
        Space O(n^2)
        
        """
        """
        def dp(s, e):
            
            if (s, e) in memo: return memo[(s, e)]
            
            if s >= e: return 0
            
            ans = sys.maxsize
            
            for k in range(s, e+1):
                next_step = max(dp(s, k-1), dp(k+1, e))
                ans = min(ans, k + next_step)
                
            memo[(s, e)] = ans
            return ans
        
        memo = {}
        return dp(1, n)
        """
        
        
        """
        Bottom up
        
        Time O(n^2)
        Space O(n^2)
        """
        
        dp = [[0] * (n+1) for _ in range(n+1)]
        
        for len in range(2, n+1):
            for i in range(1, n-len+2):
                j = i + len -1
                dp[i][j] = sys.maxsize
                
                for k in range(i, j):
                    next_step = max(dp[i][k-1], dp[k+1][j])
                    dp[i][j] = min(dp[i][j], k + next_step)
                                        
        return dp[1][n]
