class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Recursion
        
        Time Limit Exceeded
        
        """
        
#         if s == "" and p == "":
#             return True
        
#         if p == "":
#             return False
        
#         if s == "":
#             i = 0
#             while i < len(p) and p[i] == "*":
#                 i += 1
#             if i == len(p):
#                 return True
#             else:
#                 return False
            
#         # s and p:
        
#         if s[0] == p[0] or p[0] == "?":
#             return self.isMatch(s[1:], p[1:])

#         if p[0] == "*":
#             return self.isMatch(s[1:], p) or self.isMatch(s, p[1:])
        
        """
        DP
        
        Time O(n^2)
        Space O(n^2)
        
        """
    
        # s (i) row, p (j) column
        dp = [[False for j in range(len(p)+1)] for i in range(len(s)+1)]
        
        # "" matches with ""
        dp[0][0] = True
        
        # * matches with ""
        for j in range(1, len(p)+1):
            if p[j-1] != '*':
                break
            dp[0][j] = True
                
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                # match
                if p[j-1] == s[i-1] or p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                # *
                elif p[j-1] == '*':
                    # p = "a?c*"
                    # s = "abc"
                    
                    # -> p = "a?c"
                    #    s = "abc"
                    
                    # -> p = "a?c*"
                    #    s = "ab"
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                    
        return dp[-1][-1]


