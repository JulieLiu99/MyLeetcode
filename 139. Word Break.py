class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        DFS
        break out one word if it can be found in dictionary
        keep dfs for the rest of the string
        return True if any of the dfs returns True
        
        Time O(n^2)
        Space O(n^2)
        
        """
#         wordDict = set(wordDict)
#         @lru_cache(None) # must add, without will be TLE
#         def dfs(s):
#             if not s:
#                 return True
#             for i in range(1, len(s)+1): # check s[:i]
#                 if s[:i] in wordDict:
#                     if dfs(s[i:]):
#                         return True
#             return False
                
#         return dfs(s)
    
        """
        DFS + memorization
        
        """
#         n = len(s)
#         memo = {}
#         def dfs(s,loc):
#             if loc in memo:
#                 return memo[loc]
#             if s in wordDict:
#                 return True
#             start,end = loc
#             for i in range(len(s)):
#                 if dfs(s[:i],(start,start+i)) and dfs(s[i:],(start+i,end)):
#                     memo[loc] = True
#                     return True
#             memo[loc] = False
#             return False
        
#         return dfs(s,(0,n))

        """
        DP bottom up
        
        dp[i+1] = valid word breaks till s[i]
        
        Time O(n^2): where n in length of string
        Space O(n)
        
        """
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(n):
            for j in range(i+1):
                if dp[j] and s[j:i+1] in set(wordDict):
                    dp[i+1] = True
        return dp[n]
