class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        """
        Find Pivot Point and Revert to Sorted
        Time O(n)
        
        Binary Search 
        Time O(logn)
        
        Space O(1)
        
        """
        
        # find pivot index
        i = 1
        n = len(nums)
        
        while i < n and nums[i] >= nums[i-1]:
            i += 1
            
        # nums[i] < nums[i-1]
        nums = nums[i:] + nums[:i]
        
        # binary search
        l = -1
        r = n
        while l + 1 != r:
            m = l + (r-l)//2
            if nums[m] == target:
                return True
            elif nums[m] < target:
                l = m
            else:
                r = m
                
        return False
