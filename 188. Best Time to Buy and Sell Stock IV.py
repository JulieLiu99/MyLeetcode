class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        DP
        
        Same as Best Time to Buy and Sell Stock III
        
        Time O(n)
        Space O(n)
        
        """
        
        n = len(prices)
        if n < 2: return 0
        
        profits = [0] * n
        
        for _ in range(k):
            buy = prices[0] - profits[0]
            for i in range(1, n):
                buy = min(buy, prices[i] - profits[i])          # hold or buy
                profits[i] = max(profits[i-1], prices[i] - buy) # hold or sell
            
        return profits[-1]
