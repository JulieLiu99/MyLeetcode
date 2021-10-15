class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        """
        Brute Force: traverse the list once from left to right
        
        Binary Search
        if missing = (nums[m] - nums[0]) - m > k => search in left 
        if missing = (nums[m] - nums[0]) - m < k => search in right 
        
        """
        l = -1
        r = len(nums)
        
        while l + 1 != r:
            m = l + (r-l)//2
            missing = (nums[m] - nums[0]) - m
            if missing >= k:  # search in left 
                r = m
            else:  # search in right 
                l = m
                
        return nums[0] + l + k   # target is between l and r
