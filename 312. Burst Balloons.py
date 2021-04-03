class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        """
        DP: bottom up
        
        dp[i][j] is the maximum coins one can collect with balloons i ~ j
        
        Time O(n^3) 
        Space: O(n^2)
        
        """
        
        nums = [1] + nums + [1] 
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for d in range(2, n):
            for i in range(0, n-d):
                j = i + d
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], 
                                   nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
        return dp[0][n-1]

        
        """
        DP: top down, recursion + memorization
        
        time exceeded
        """
        """
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        @lru_cache(maxsize=None)
        def calculate(i, j):
            if dp[i][j] or j == i + 1:
                return dp[i][j]
            coins = 0
            for k in range(i+1, j): 
                coins = max(coins, 
                            nums[i] * nums[k] * nums[j] + calculate(i, k) + calculate(k, j))
            dp[i][j] = coins
            return coins

        return calculate(0, n-1)
        """
