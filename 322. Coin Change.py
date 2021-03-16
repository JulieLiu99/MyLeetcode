class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        """
        Dinamic programming https://www.youtube.com/watch?v=ZI17bgz07EE
        
        dp[i] is the fewest number of coins making up amount i
        For every coin in coins, dp[i] = min(dp[i], dp[i - coin] + 1)

        Time complexity O(amount * coins.length)
        Space complexity O(amount)
        
        """
        
        dp = [0] + [float('inf') for i in range(amount)]
        
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
                    
        if dp[-1] == float('inf'):
            return -1
        
        return dp[-1]
