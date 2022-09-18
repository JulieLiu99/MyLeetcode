class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        """
        Greedy
        
        Sort from small to large.
        Go through array. 
        At any point, +k to the smaller half and -k to the larger half.
        
        l x x x a | b x x x r
            +k    ^    -k
            
        The min could be either l+k or b-k
        The max could be either r-k or a+b
        
        Optimization is to:
        Return orignal range r-l if it's smaller than k already, e.g. [2, 4], k = 5
        """
        
        nums.sort()
        res = nums[-1] - nums[0]
        
        if res <= k: 
            return res
        
        for i in range(len(nums) - 1): # the middle |
            a, b = nums[i], nums[i+1]
            cur_max = max(nums[-1] - k, a + k)
            cur_min = min(nums[0] + k, b - k)
            res = min(res, cur_max - cur_min)
        return res
