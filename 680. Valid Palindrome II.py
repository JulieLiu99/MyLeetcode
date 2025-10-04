class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Two Pointers
        Move from two ends to center as long as characters are matching

        Whenever characters are not matching
        Delete char on either left pointer or right pointer
        
        Time O(n): two pointers go through string once, reverse O(substring)
        Space O(1): with reverse substring becomes O(n), could be reduced to O(1)
        
        """
        l = 0
        r = len(s) - 1
        
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                # delete left or delete right
                return s[l:r] == s[l:r][::-1] or s[l+1:r+1] == s[l+1:r+1][::-1]
        return True
