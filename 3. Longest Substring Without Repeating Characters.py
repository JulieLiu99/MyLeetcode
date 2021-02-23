class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        """
        Time O(n)
        Space O(n)
        
        """
        
        n = len(s)
        ans = 0
        # mp stores the current next index of a character
        mp = {}

        i = 0
        
        # try to extend the range [i, j]
        
        for j in range(n):  # j is the right pointer
            if s[j] in mp:  # checking can be done in O(1)
                i = max(mp[s[j]], i)    # update i, left pointer
                                        # if s[j] is to the right side of i

            ans = max(ans, j - i + 1)   # update the range [i, j]
            mp[s[j]] = j + 1

        return ans
