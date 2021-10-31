class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[-1] > nums[0]: # increasing            
            return all(nums[i] <= nums[i + 1] for i in range(0, len(nums) - 1))

        else: # decreasing
            return all(nums[i] >= nums[i + 1] for i in range(0, len(nums) - 1))
