class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary Search
        
        Let's say nums looks like this: 
        [12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        Because it's not fully sorted, we can't do normal binary search. But here comes the trick:

        If target is 14, ignore right side:
        [12, 13, 14, 15, 16, 17, 18, 19, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]

        If target is 7, ignore left side:
        [-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

        Compare both the target and the mid element against nums[0].
        If not "on the same side", ignore the half away from target.
        Once nums[mid] and target are "on the same side" of nums[0], do ordinary binary search.
        
        Time O(logn)
        Space O(1)
        
        """
        
        l, r = 0, len(nums)

        while l < r:
            
            mid = l + (r-l)// 2
            
            # nums[mid] and target are "on the same side" of nums[0]
            # do ordinary binary search
            if (nums[mid] < nums[0]) == (target < nums[0]):
                if (nums[mid] < target):
                    l = mid + 1
                elif (nums[mid] > target):
                    r = mid
                else:
                    return mid
                
            elif target < nums[0]:
                l = mid + 1
                
            else:
                r = mid

        return -1
