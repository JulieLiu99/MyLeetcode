class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        """
        Brute Force
        Two pointers l and r
        For each l, use r to scan rest of s
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
        
#         while l < n:
#             temp = t[:]
#             while r < n:
#                 if s[r] in temp:
#                     temp = temp.replace(s[r], '', 1)  # match
#                     if temp == "":  # all matched
#                         if not res or r-l+1 < len(res):
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

        countT = collections.Counter(t)
        need = len(countT)
        
        window = collections.defaultdict(int)
        have = 0
        res = ""
        l = 0
        
        for r in range(len(s)):
            if s[r] in countT:
                window[s[r]] += 1
                if window[s[r]] == countT[s[r]]:
                    have += 1
            while have == need: # update result and move l
                if not res or r-l+1 < len(res):
                    res = s[l:r+1]

                if s[l] in countT: # pop from left of window
                    window[s[l]] -= 1
                    if window[s[l]] < countT[s[l]]:
                        have -= 1
                l += 1
            
        return res
