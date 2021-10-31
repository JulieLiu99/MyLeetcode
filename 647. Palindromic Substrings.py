class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Check all substrings
        
        Time O(n^3)
        
        """
#         @lru_cache(None)
#         def isPalindrome(i, j):
#             if i > j: return True
#             if s[i] != s[j]: return False
#             return isPalindrome(i+1, j-1)
        
#         n = len(s)
#         rse = 0
#         for i in range(n):
#             for j in range(i, n):
#                 if isPalindrome(i, j):
#                     res += 1
#         return res
    
        """
        Expand around centers
        
        Time O(n^2)
        
        """
        n = len(s)
        count = 0
        for start_left in range(n):
            for start_right in [start_left, start_left + 1]:
                l, r = start_left, start_right
                while l >= 0 and r < n and s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
        
        return count
