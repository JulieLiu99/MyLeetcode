class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        char + ... + char
        Count letters in between

        Time O(n)
        Space O(1)
        """
        letters = set(s)
        ans = 0
        
        for letter in letters:
            i, j = s.index(letter), s.rindex(letter)
            middle_letters = set()
            
            for k in range(i + 1, j):
                middle_letters.add(s[k])
            
            ans += len(middle_letters)

        return ans
