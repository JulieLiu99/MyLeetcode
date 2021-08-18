class Solution:
    def minCut(self, s: str) -> int:
        
        """
        Backtracking, Recursion DFS
        
        TLE
        
        Time O(n^3)
        Space O(n)
        
        """
#         def isPalindrome(s):
#             l = 0
#             r = len(s)-1
#             while l <= r:
#                 if s[l] == s[r]:
#                     l += 1
#                     r -= 1
#                 else:
#                     return False
#             return True
        
#         self.res = float('inf')
        
#         @lru_cache(None)
#         def dfs(s, cut):
#             if s == "":
#                 self.res = min(self.res, cut-1)
#                 return 
#             for i in range(len(s)):
#                 if isPalindrome(s[:i+1]):
#                     dfs(s[i+1:], cut+1)
                
#         dfs(s, 0)
#         return self.res

        
        """
        1. Replace isPalindrome(s) with if sequence == sequence[::-1]
        2. Pass i instead of s to the recursion function
        
        still TLE
        
        Time O(n^3)
        Space O(n^2)
        
        """
#         self.res = float('inf')
        
#         @lru_cache(None)
#         def dfs(i, cut):
#             if i == len(s):
#                 self.res = min(self.res, cut-1)
#                 return 
#             for j in range(i, len(s)):
#                 sequence = s[i:j+1]
#                 if sequence == sequence[::-1]:
#                     dfs(j+1, cut+1)
                
#         dfs(0, 0)
#         return self.res


        """
        DP bottom up
        
        Time O(n^3)
        Space O(n^2)
        
        """
#         n = len(s)
#         res = [0] + [i+1 for i in range(n)] # res[1,...,n] actually useful
        
#         for i in range(n):
#             for j in range(i, n):   # s[i...j]
#                 sequence = s[i:j+1] # can't use s[i:j+1] == s[j:i-1:-1] because 0 -> -1
#                 if sequence == sequence[::-1]: 
#                     res[j+1] = min(res[j+1], res[i]+1, res[j]+1)
#                 else:
#                     res[j+1] = min(res[j+1], res[j]+1)

#         return res[-1] - 1

        """
        Optimized DP bottom up
        
        if sequence == sequence[::-1]: 
            res[j+1] = min(res[j+1], res[i]+1, res[j]+1)
        else:
            res[j+1] = min(res[j+1], res[j]+1)
            
        res[j]+1 is unnecessary because when i = j, s[i] is Palindrome, res[i]+1 = res[j]+1
        else is unnecessary for the same reason
        
        Time O(n^3)
        Space O(n)
        
        """

        n = len(s)
        res = [_ for _ in range(-1, n)] # res[1,...,n] actually useful
        
        for i in range(n):
            for j in range(i, n):   # s[i...j]
                sequence = s[i:j+1] # can't use s[i:j+1] == s[j:i-1:-1] because 0 -> -1
                if sequence == sequence[::-1]: 
                    res[j+1] = min(res[j+1], res[i]+1)

        return res[-1] 

