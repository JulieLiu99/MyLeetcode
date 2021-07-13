class Solution:
    def numDecodings(self, s: str) -> int:
        """
        DFS - recursion
        
        Time O(n^2)
        Space O(n^2)
        
        TLE
        
        """
        
#         nums = set()
#         for x in range(1, 27): nums.add(str(x))
#         n = len(s)
#         self.res = 0
        
#         def dfs(i):

#             if i == n:
#                 self.res += 1
#                 return 
                
#             if s[i] in nums:
#                 dfs(i+1)
            
#             if i<=n-2 and s[i:i+2] in nums:
#                 dfs(i+2)
                
#         dfs(0)
#         return self.res


        """
        Recursion with Optimization
        
        Works with @lru_cache(maxsize=None)
        
        """


#         n = len(s)
        
#         @lru_cache(maxsize=None)
#         def dfs(i):

#             if i == n:
#                 return 1
            
#             if s[i] == "0": 
#                 return 0
            
#             if i<=n-2 and int(s[i:i+2]) <= 26:
#                 return dfs(i+1) + dfs(i+2)
#             else:
#                 return dfs(i+1)
        
#         return dfs(0)


        """
        DP, iterative 
        
        Time O(n)
        Space O(n)
        
        """

        # dp[i+1] = result up to i, where i = 0...len(s)-1
        dp = [0 for _ in range(len(s) + 1)] 

        # base case initialization
        dp[0] = 1 
        
        if s[0] == "0":
            dp[1] = 0
        else:
            dp[1] = 1

        for i in range(2, len(s) + 1): 

            if 0 < int(s[i-1:i]) <= 9:    
                dp[i] += dp[i - 1]

            if 10 <= int(s[i-2:i]) <= 26: 
                dp[i] += dp[i - 2]
                
        return dp[len(s)]
    
