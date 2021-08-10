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
                # profit_now = price_now - price_bought + profit_prev
                #            = price_now - (price_bought - profit_prev)
                buy = min(buy, prices[i] - profits[i])          # hold the prev stock or buy the stock today instead
                profits[i] = max(profits[i-1], prices[i] - buy) # hold the current stock or sell the stock today
            
        return profits[-1]