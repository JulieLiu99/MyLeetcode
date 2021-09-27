class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Sliding Window
        
        Time O(N)
        Space O(1)
        
        """
        res = len(nums) + 1
        i = 0
        for j in range(len(nums)):
            target -= nums[j]
            while target <= 0: # elements seen so far have reached sum
                res = min(res, j - i + 1)
                target += nums[i]
                i += 1
        return res % (len(nums) + 1)
