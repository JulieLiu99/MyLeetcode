class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Dynamic programming: https://www.youtube.com/watch?v=DJ4a7cmjZY0
        
        Time O(n * amount)
        Space O(n)
        
        """
        
        dp = [1] + [0] * amount  
        
        for i in coins:
            
            for j in range(i, amount + 1):
                
                   dp[j] += dp[j - i]
                    
        return dp[amount]
