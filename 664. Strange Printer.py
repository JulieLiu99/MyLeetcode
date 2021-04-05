class Solution:
    def strangePrinter(self, s: str) -> int:
        
        """
        DP: top down, recursion + memorization
        "bottom up is hard?"
        
        dp(i, j): minimum number of turns to print letter s[j] within i~j
        
        works
        
        Time O(n^3)
        Space O(n^2)
        
        """
        
        memo = {}
        def dp(i, j):
            if i > j: return 0
            if (i, j) not in memo:
                ans = dp(i+1, j) + 1
                for k in range(i+1, j+1):
                    if s[k] == s[i]:
                        ans = min(ans, dp(i, k-1) + dp(k+1, j))
                memo[i, j] = ans
            return memo[i, j]

        return dp(0, len(s)-1)
