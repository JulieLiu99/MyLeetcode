class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Binary search
        
        Time O(logn)
        Space O(1)
        
        """
        l = 0
        r = len(nums)-1
        
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
                
        return l
