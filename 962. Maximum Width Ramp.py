class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        """
        Intuition:
        
        Keep a stack of idexes of mono decreasing nums.
        When the number is smaller the the last,
        push it into the stack.
        
        For each number,
        pop till we find the first smaller number in the stack.
        update the width of ramp.

        Time O(N)
        Space O(N)
        
        """
        dec_stack = []
        res = 0
        
        for i, num in enumerate(nums):
            if not dec_stack or num < nums[dec_stack[-1]]:
                dec_stack.append(i)
                
        for j in range(len(nums)-1, -1, -1):
            while dec_stack and nums[j] >= nums[dec_stack[-1]]:
                res = max(res, j - dec_stack.pop())
                
        return res
        
        """
        Brute Force
        
        Sort nums in increasing order.
        Loop through nums, update max(res, i - imin) and min(imin, i).
        
        Time O(NlogN)
        Space O(N)
        
        """
#         increasing = [(num, i) for i, num in enumerate(nums)]
#         increasing.sort()

#         imin = float('Inf')
#         res = 0
#         for num, i in increasing:
#             res = max(res, i - imin)
#             imin = min(imin, i)

#         return res
