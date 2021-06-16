class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        """
        Mono Incrasing Stack

        We want to get a subsequence of small nums.
        Keep a mono incrasing stack as result.
        
        If current element num is smaller than the last element in the stack,
        replace it to get a smaller sequence.

        Before we do this, check if there are enough elements.
        After popping the last element from stack,
        we would have len(stack) - 1 in the stack,
        and len(nums) - i that can be pushed into stack.
        if len(stack) - 1 + len(nums) - i >= k, ok to pop from stack.

        Then, if the stack not full with k element,
        push nums[i] into the stack.

        Time O(n)
        Space O(k)
        
        """
        
        stack = []
        
        for i, num in enumerate(nums):
            
            while stack and stack[-1] > num and len(stack) - 1 + len(nums) - i >= k:
                stack.pop()
                
            if len(stack) < k:
                stack.append(num)
                
        return stack
