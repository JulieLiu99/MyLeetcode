class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        DP - recursion
        
        TLE
        """
        
#         self.res = 0

#         n = len(t)  # length of target
        
#         @lru_cache(None) # CANNOT USE THIS -> ERASES self.res VALUE
#         def dp(s, i):
#             if i == n:  # target string matched till end
#                 self.res += 1
#                 return 
            
#             for j in range(len(s)):
#                 if s[j] == t[i]:
#                     dp(s[j+1:], i+1)
                                                
#         dp(s, 0)
#         return self.res
    
        
        
#         self.res = 0

#         n_s = len(s)
#         n = len(t)  # length of target
        
#         # @lru_cache(None) # CANNOT USE THIS -> ERASES self.res VALUE
#         def dp(si, i):
#             if i == n:  # target string matched till end
#                 self.res += 1
#                 return 
            
#             for j in range(si, n_s):
#                 if s[j] == t[i]:
#                     dp(j+1, i+1)
                                                
#         dp(0, 0)
#         return self.res

        """
        DP - recursion
        
        Need to find a way to use @lru_cache(None)
        """
#         @lru_cache(None)
#         def dp(i, j):
            
#             if j == len(t):
#                 return 1
            
#             if i == len(s):
#                 return 0
            
#             count = 0
#             if s[i] == t[j]:
#                 count += dp(i+1, j+1)
                
#             count += dp(i+1, j)
#             return count
        
#         return dp(0, 0)
        
        """
        DP - bottom up
        
        Time O(n_s * n_t)
        Space O(n_s * n_t)
        
        """
        
        n_s = len(s)
        n_t = len(t)
        
        dp = [[0] * (n_t+1) for _ in range(n_s+1)]
        
        for i in range(n_s+1):
            dp[i][0] = 1 # when t is empty, we always have 1
            
        for i in range(1, n_s+1):
            for j in range(1, n_t+1):
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]*(s[i-1] == t[j-1])
                
        return dp[-1][-1]
