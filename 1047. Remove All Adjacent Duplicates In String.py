class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        Stack
        
        Notice that we can't just go through s once
        Because after removal of one pair, we might create new adjacent duplicates
        
        With a stack, always compare the top element with next element,
        If top elemented popped, top becomes the one previous c
        
        Time O(n)
        Space O(n)
        
        """
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
