class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Approach 4: Expand Around Center
        Time O(n^2): expanding a palindrome around its center could take O(n), so overall complexity is O(n^2)
        Space O(1): no extra storage other than some constant variables
        """
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]
