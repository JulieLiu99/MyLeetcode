class Solution:
    def isValid(self, s: str) -> bool:
        
        """
        Time O(n)
        Space O(n)
        """

        bracket_map = {"(": ")", "[": "]",  "{": "}"}
        stack = []  # storing unclosed brackets
        
        for i in s:
            if i in bracket_map.keys():
                stack.append(i)
            elif stack and i == bracket_map[stack[-1]]:
                    stack.pop()
            else:
                return False
            
        return stack == [] 
