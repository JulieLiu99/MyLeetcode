from copy import copy

class Solution:
    def balancedString(self, s: str) -> int:
        
        """
        My own solution: one pass for counting, one pass for finding subarray
        Time O(n^2): for each start, loop through to find subarray
        Space O(n): for each possible subarray, copy dict of size 4
        
        """
        
        """
        chars = collections.defaultdict(int)
        n = len(s)
        
        for char in s:
            chars[char] += 1
        if len(chars.keys()) == 1: return int(n/4*3)
        
        to_replace = collections.defaultdict(int)
        for key in chars.keys():
            if chars[key] > n/4:
                to_replace[key] += int(chars[key] - n/4)
        if not to_replace: return 0
        
        replace = n
        for start in range(n):
            if s[start] in to_replace:
                end = start     # start is last good one
                cur_to_replace = copy(to_replace)
                while end < n and cur_to_replace:
                    if s[end] in cur_to_replace:
                        cur_to_replace[s[end]] -= 1
                        if cur_to_replace[s[end]] == 0:
                            del cur_to_replace[s[end]]
                    end += 1
                if not cur_to_replace:
                    replace = min(replace, end-start)
                
        return replace
                    
        """
        
        """
        Sliding window from two ends, till the min subarray is reached
        Time O(N), one pass for counting, one pass for sliding window
        Space O(1)

        """
        count = collections.Counter(s)
        n = len(s)
        if all(n/4 == count[c] for c in 'QWER'): return 0
        
        res = n
        i = 0
        for j, c in enumerate(s):
            count[c] -= 1
            while i <= j and all(n/4 >= count[c] for c in 'QWER'):
                res = min(res, j - i + 1)
                count[s[i]] += 1
                i += 1
        return res
