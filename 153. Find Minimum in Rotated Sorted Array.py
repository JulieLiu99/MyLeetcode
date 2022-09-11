class Solution:
    def findMin(self, nums: List[int]) -> int:

        """
        Binary search
        
        if nums[m] > nums[-1] we know min is on right side,
        otherwise middle should have been smaller than right
        
        l for increasing part before min
        r for min and increasing part after it
        """
        l = -1
        r = len(nums)
        while l + 1 != r:
            m = (l + r) // 2
            if nums[m] > nums[-1]: # min on right side
                l = m
            else:
                r = m
            
        return nums[r]
