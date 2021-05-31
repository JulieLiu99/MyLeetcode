class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        """
        Stack
        
        Time O(n)
        Space O(n)
        
        """
        
        stack = [0]
        longest = 0
        
        for c in s:
            if c == "(":
                stack.append(0)
            else:   # )
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2    # add this ()
                    longest = max(longest, stack[-1])
                else:
                    stack = [0]     # invalid ), restart from length 0

        return longest
