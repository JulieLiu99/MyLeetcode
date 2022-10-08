class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Sliding Window
        
        Time O(N)
        Space O(1)
        
        """
        n = len(nums)
        cur_sum = 0
        i = 0
        res = n + 1 # impossible, always larger than any valid answer
        for j in range(len(nums)):
            cur_sum += nums[j]
            while cur_sum >= target:
                res = min(res, j - i + 1)
                cur_sum -= nums[i]
                i += 1
                
        if res == n + 1:
            return 0
        else:
            return res