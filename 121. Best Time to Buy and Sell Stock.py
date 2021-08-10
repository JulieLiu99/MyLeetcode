class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        """
        Brute Force: for every day to buy, check every day to sell
        Time O(n^2)
        
        Two Pointers
        One pass through the prices list
        
        if prices[r] < prices[l]:
            move l to r, and r to l+1
        if prices[r] > prices[l]:
            update res
            move r one step right
            
        Time O(n)
        Space O(1)
        
        """
        
        res = 0
        n = len(prices)
        if n == 1: 
            return 0
        
        l = 0
        r = 1
        
        while l<r<n:
            if prices[r] < prices[l]:
                l = r
                r = l + 1
            else:
                res = max(res, prices[r] - prices[l])
                r += 1
        
        return res
