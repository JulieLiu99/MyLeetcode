class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Two pointers
        Keep track of chars and indices last seen
        
        a b c a ...
          ^ ^ ^
        window without repeating char

        Time O(n)
        Space O(n)
        """
        left = 0 # start of current window
        seen = {} # char: idx
        ans = 0

        for right, char in enumerate(s):
            if char in seen:
                # start window from where char was last seen
                left = max(left, seen[char] + 1)  
            ans = max(ans, right - left + 1)
            seen[char] = right
        return ans
