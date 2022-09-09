class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        1. Both should have the same characters
        2. Difference should be either 0, no swap, or 2, one swap.
        
        Time O(n)
        Space O(n)
        
        """
        diff = 0
        for ch1, ch2 in zip(s1, s2):
            if ch1 != ch2: 
                diff += 1
        return (Counter(s1) == Counter(s2)) and (diff == 0 or diff == 2)
