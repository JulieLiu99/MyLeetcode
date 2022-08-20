class Solution:
    
    # Compute in-place, row by row
    
    # Time O(n^2)
    # Space O(1)
    
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        while n > 1:
            for i in range(n-1):
                nums[i] = (nums[i] + nums[i+1]) % 10
            nums.pop()
            n -= 1
        return nums[0]
