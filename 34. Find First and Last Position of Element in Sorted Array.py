class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        """
        Binary Search 
        
        O(logn)
        O(1)
        
        """
        
        # Solution 1. use Python bisect library
        
#         l = bisect.bisect_left(nums,target)
#         r = bisect.bisect_right(nums,target)
#         return [-1, -1] if l == r else [l, r - 1]


        # Solution 2. write own binary search functions
    
        if not nums:
            return [-1, -1]

        def bisect_left(nums, target):  # [l, r)
            l, r = 0, len(nums) - 1
            while l < r:
                m = l + (r - l) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l if nums[l] == target else -1

        def bisect_right(nums, target): # (l, r]
            l, r = 0, len(nums) - 1
            while l < r:
                m = l + (r - l + 1) // 2
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m
            return r if nums[r] == target else -1

        return [bisect_left(nums, target), bisect_right(nums, target)]
