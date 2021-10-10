class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        """
        Minimum Add to Make Parentheses Valid
        = Number of Invalid Parentheses
        ^
        Because we can't move things around, so whatever is extra, we add a complement to make it valid
        
        Time O(n)
        Space O(1)
        
        """
        
        left = 0
        right = 0
        
        for c in s:
            if c == "(":
                left += 1
            else:
                if left:
                    left -= 1
                else:
                    right += 1
                    
        return left + right
