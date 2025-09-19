class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Stack

        Iterate through s
        Whenever there is a (, add to stack
        Whenever there is a ), pop the most recent ( from stack to form a pair
        - If no matching (, the ) should be deleted
        - If there are unmatched ('s in the end, they should be deleted

        How to delete?
        Convert string to list and join list back to str in the end.
        String is an immutable data structure in Python and it's much easier and memory-efficient to update a list.

        Time O(n)
        Space O(n)
        
        """
        s = list(s)
        stack = []
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''       # remove extra )
                    
        while stack:
            s[stack.pop()] = ''     # remove extra (
            
        return ''.join(s)
