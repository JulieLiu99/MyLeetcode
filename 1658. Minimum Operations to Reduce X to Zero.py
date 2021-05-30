class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        """
        
        Prefix Sum + Hashmap
        
        We need to remove minimum number of values from the beginning and end, such that sum of rest is equal to x. 
        
        It is equivalent to finding one max-length subarray, whose sum equals goal = sum(nums) - x. 
        
        Instead of prefix sum, this question uses cummulative sum where
        cumsum_idx[sum] = i means nums[0] + nums[1] + ... + nums[i] = sum.
        
        Length of subarray window: cumsum_idx[num] - cumsum_idx[num-goal].
        
        Time O(n)
        Space O(n)
        
        """
        
        cum_sum = 0
        cumsum_idx = {cum_sum: -1}
        for i, num in enumerate(nums):
            cum_sum += num
            cumsum_idx[cum_sum] = i
                
        goal = cum_sum - x
        ans = -1

        if goal < 0: return -1

        for num in cumsum_idx:
            if num - goal in cumsum_idx:
                ans = max(ans, cumsum_idx[num] - cumsum_idx[num-goal])

        return len(nums) - ans if ans != -1 else -1
