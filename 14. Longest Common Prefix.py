class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Horizontal scanning
        Time Complexity: O(S), where S is the sum of all the characters in the list. In the worst case scenario, the words are all the same.
        Space Complexity: O(1)

        """
        if not strs:
            return ""
        
        shortest = min(strs,key=len)
        
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 
