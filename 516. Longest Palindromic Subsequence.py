class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        """
        DP
        dp[i][j]: solution for s[i...j]
        
        Time O(n^2)
        Space O(n^2)
        
        
        Note: Cannot do linear span and expand from each center
        because [subsequence] does not have to be continous!
        
        Reversely, for substring cannot do DP 
        because dp's outer cells can inherit noncontinous inner palindrome
        
        """
        
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]
        
        for l in range(1, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                if i == j:                      # a
                    dp[i][j] = 1
                elif s[i] == s[j]:              # a***a
                    dp[i][j] = dp[i+1][j-1] + 2
                else:                           # a*** OR ***a
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][-1]
                    
    
        # THIS DOES NOT WORK
#         max_len = 0
#         n = len(s)
#         for center in range(n):
#             for l, r in [(center, center), (center, center+1)]: # either odd or even length
#                 while l >= 0 and r <= n-1 and s[l] == s[r]: # expand
#                     max_len = max(max_len, r-l+1)
#                     l -= 1
#                     r += 1
#         return max_len
