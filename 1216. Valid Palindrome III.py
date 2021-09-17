class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        """
        Brute Force
        Remove all possible combinations of k
        And check if rest of string is valid
        
        Time O(n!/((n-k)!k!) * n)
        Space O(1)
        
        """
        
        """
        Iterative DP
        
        Time O(n^2)
        Space O(n^2)
        
        " a (b) c d (e) c a "
            
        c a 1
        e c 1   e a 2
        d e 1   d c 2   d a 3
        c d 1   c e 2   c c 1   c a 2
        b c 1   b d 2   b e 3   b c 2   b a 3
        a b 1   a c 2   a d 3   a e 4   a c 3   a a 2
        
        """
        n = len(s)
        dp_array = [[0 for i in range(n)] for j in range(n)]
        
        for l in range(n-2, -1, -1):
            for r in range(l+1, n):
                if(s[l] == s[r]):
                    dp_array[l][r] = dp_array[l+1][r-1]
                else:
                    dp_array[l][r] = 1 + min(dp_array[l+1][r], dp_array[l][r-1])

        return dp_array[0][n-1] <= k
    

        """
        Recursive DP
        
        dp[i][j]: the number of removal down in order to make s[i~j] palindrome
        
        Time O(n^2)
        Space O(n^2)
        
        """
#         n = len(s)
#         dp = [[-1 for _ in range(n)] for i in range(n)]
#         removal = self.dfs(s, 0, n-1, dp)
#         return removal <= k
        
#     def dfs(self, s, i, j, dp):
        
#         if dp[i][j] != -1: # visited
#             return dp[i][j]
        
#         if i == j: # end of check
#             dp[i][j] = 0
#             return 0
        
#         if i == j - 1: # last step
#             dp[i][j] = 0 if s[i] == s[j] else 1
#             return dp[i][j]
        
#         if s[i] == s[j]: # match, removal = removal to make inner substring palindrome
#             dp[i][j] = self.dfs(s, i+1, j-1, dp)
#             return dp[i][j]
        
#         else: # don't match, remove either left char or right char here
#             dp[i][j] = min(self.dfs(s, i+1, j, dp), self.helper(s, i, j-1, dp)) + 1
#             return dp[i][j]


