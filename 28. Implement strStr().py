class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Time O(n*m): string comparison is O(m) done O(n) times
        Space O(1)
        """
        
        for i in range(len(haystack) - len(needle)+1):
            
            if haystack[i:i+len(needle)] == needle:
                return i
            
        return -1
