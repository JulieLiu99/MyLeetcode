class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        """
        DP: bottom up
        
        dp[i][j] is the minimum cost to cut between A[i] and A[j]
        
        Time O(N^3)
        Space O(N^2)
        
        """
        """
        cuts = sorted(cuts + [0, n])
        length = len(cuts)
        
        dp = [[10**9] * length for _ in range(length)]
        for _ in range(length-1):
            dp[_][_+1] = 0
            
        for d in range(2, length):
            for i in range(0, length-d):
                j = i + d
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cuts[j] - cuts[i])

        return dp[0][length-1]
        """
        
        """
        DP: top down, recursion + memory
        
        Also works!
        """
        
        cuts = sorted(cuts + [0, n])
        @functools.lru_cache(None)
        def dp(i, j):
            if j - i <= 1: return 0
            return cuts[j] - cuts[i] + min((dp(i, k) + dp(k, j) for k in range(i+1, j)), default=0)
        return dp(0, len(cuts)-1)
