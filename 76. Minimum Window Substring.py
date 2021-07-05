class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        """
        Brute Force
        Two pointers l and r
        For each l, use l to scan rest of s
        Record char in s[l:r+1] that matches with char in t
        If t all matched, update res
        
        Time Limit Exceeded :(
        Time O(len(s)^2 * len(t))
        Space O(len(t))
        
        """
#         n = len(s)
#         m = len(t)
#         if n < m: return ""
            
#         l = 0
#         r = 0
#         res = ""
        
#         while l<=n-1:
#             temp = t[:]
#             while r<=n-1:
#                 if s[r] in temp:
#                     temp = temp.replace(s[r], '', 1)  # remove s[r] from temp
#                     if temp == "":
#                         if res == "":
#                             res = s[l:r+1]
#                         elif r-l+1 < len(res):
#                             res = s[l:r+1]
#                 r += 1
#             l += 1
#             r = l
            
#         return res

        """
        Two dictionaries, one for t, one for s
        
        Scan t once, record all chars
        Scan s once, also using two pointers l, r
        Compare window with countT (if have == need) to update res and l
        
        Time O(len(s) + len(t))
        Space O(len(s) + len(t))
        
        """

        countT = collections.defaultdict(int)
        window = collections.defaultdict(int)
        for c in t:
            countT[c] += 1
            
        have = 0
        need = len(countT)
        res = ""
        l = 0
        
        for r in range(len(s)):
            if s[r] in countT:
                window[s[r]] += 1
                if window[s[r]] == countT[s[r]]:
                    have += 1
            while have == need: # update result and try to move l
                if res == "":
                    res = s[l:r+1]
                elif r-l+1 < len(res):
                    res = s[l:r+1]
                # pop from the left of window
                if s[l] in countT:
                    window[s[l]] -= 1
                    if window[s[l]] < countT[s[l]]:
                        have -= 1
                l += 1
            
        return res
