class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        """
        DP
        
        dp[index][diff]: length of arithmetic sequence at index with difference diff

        Time O(N^2)
        Space O(N^2)
        
        [3,6,9,12]:
        
        [{}, {3: 2}, {6: 2, 3: 3}, {9: 2, 6: 2, 3: 4}]
        
        """
        
        max_len = 0
        dp = [{} for _ in range(len(nums))]  # index: {diff: curr_max_len}
        for i in range(1, len(nums)): # ... - j - i
            for j in range(0, i):
                diff = nums[i] - nums[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2
                max_len = max(max_len, dp[i][diff])
        return max_len
