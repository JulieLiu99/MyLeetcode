class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        """
        DP
        
        At each index, keep track of the maximum sum using DP table
        - either add the previous subarray
        - or just the current num
        Return the maximum out of the table
        
        Time O(n)
        Space O(n)
        
        """
        dp = [0]*len(nums)
        for i, num in enumerate(nums):            
            dp[i] = max(dp[i-1] + num, num)
        return max(dp)


