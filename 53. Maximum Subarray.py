class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        DP table
        to keep track of maximum sum at each index

        Time O(n)
        Space O(n)
        """
        # dp = [0]*len(nums)
        # for i, num in enumerate(nums):            
        #     dp[i] = max(dp[i-1] + num, num)
        # return max(dp)

        """
        DP only keep track of max sum
        
        At each index, either
        - extend the previous subarray
        - or, start a new one with the current num

        Time O(n)
        Space O(1)
        """
        max_sum = nums[0]
        current_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(current_sum + num, num)
            max_sum = max(max_sum, current_sum)

        return max_sum

