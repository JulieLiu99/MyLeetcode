class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        """
        l ... r
        
        """
        nums.sort()
        l = 0
        r = len(nums)-1
        res = -1
        
        while l < r:
            if nums[l] + nums[r] < k:
                res = max(res, nums[l] + nums[r])
                l += 1
            else:
                r -= 1
                
        return res
