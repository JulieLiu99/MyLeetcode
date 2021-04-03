class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        """
        DP: bottom up
        
        
        dp[l][r] means the minimum score to triangulate values[l] ~ values[r],
        where there is edge connecting values[l] and values[r].

        Enumerate all points values[k] with l < k < r to form a triangle

        Score is dp[l][r], dp[l][k] + dp[k][r] + values[l]*values[r]*values[k]
        
        Time O(n^3)
        Space O(n^2)
        
        """
        
        n = len(values)
        dp = [[0]*n for i in range(n)]
        for d in range(2, n):
            for l in range(0, n-d):
                r = l + d
                dp[l][r] = float("Inf")
                for k in range(l+1, r):
                    dp[l][r] = min(dp[l][r], 
                                   dp[l][k] + dp[k][r] + values[l]*values[r]*values[k])
        return dp[0][-1]
    
    
        """
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                memo[i, j] = min([dp(i,k) + dp(k,j) + values[i]*values[j]*values[k] for k in range(i+1, j)] or [0])
            return memo[i, j]
        return dp(0, len(values) - 1)
        """
