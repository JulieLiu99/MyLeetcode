class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        Naive swap
        Time O(n^2) TLE
        """
        
#         n = len(nums)
#         for i in range(n):
#             if nums[i] == 0:
#                 j = i + 1
#                 while j < n and nums[j] == 0:
#                     j += 1
#                 if j < n: nums[i], nums[j] = nums[j], nums[i] # swap

        """
        Record number of 0 while scanning
        Move nonzeros to the front while scanning
        
        Time O(n)
        Space O(1)
        
        """
        zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                nums[i-zeros] = nums[i]
                
        if zeros: nums[-zeros:] = [0] * zeros
