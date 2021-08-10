class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        DP
        
        res[i] = max profit till day i, in the current round of stock transection
        
        Time O(n)
        Space O(n)
        """
        
        n = len(prices)
        if n == 1: return 0
        
        profits = [0] * n
        
        for k in range(2):
            
            buy = prices[0] - profits[0] # buy on first day
            
            for i in range(1, n):
                buy = min(buy, prices[i]-profits[i])            # hold the stock, or buy today instead
                profits[i] = max(profits[i-1], prices[i] - buy) # don't do anything, or sell today
                
        return profits[-1]
