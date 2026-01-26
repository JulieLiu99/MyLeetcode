class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Brute Force: for every day to buy, check every day to sell
        Time O(n^2)

        Two Pointers
        One pass through the prices list
        
        Keep track of 
        - Min price so far to buy
        - Max possible profit from selling at each day
            
        Time O(n)
        Space O(1)
        """
        profit = 0
        min_price = float('inf')

        if not prices:
            return 0

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit
