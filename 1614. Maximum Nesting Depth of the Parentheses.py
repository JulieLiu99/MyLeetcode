class Solution:
    def maxDepth(self, s: str) -> int:
        """
        The depth equals to the maximum open parentheses.
        
        Time O(N)
        Space O(1)
        
        """
        res = 0
        cur_depth = 0
        for c in s:
            if c == '(':
                cur_depth += 1
                res = max(res, cur_depth)
            if c == ')':
                cur_depth -= 1
        return res
