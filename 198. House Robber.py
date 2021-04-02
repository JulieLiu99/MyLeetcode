class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        DP: bottom up
        either skip one or skip two
        Time O(n)
        Space O(1)
        
        """
        nums = [0, 0, 0] + nums
        for i in range(3, len(nums)):
            r2 = nums[i-2] + nums[i]
            r3 = nums[i-3] + nums[i]
            nums[i] = max(r2, r3) + nums[i]
        return max(nums)
