class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        """
        Two Pointers
        One Pass
        
        Whenever we have prices[r] > prices[l],
        We buy on day l and sell on day r.
        Increment res by prices[r] - prices[l].
        Move right:
        l = r
        r = l + 1
        
        If prices[r] > prices[l],
        Don't do anything and just move right:
        l = r
        r = l + 1
        
        Time O(n)
        Space O(1)
        
        """
        
        n = len(prices)
        if n == 1:
            return 0
        
        l = 0
        r = 1
    
        res = 0
        
        while l < r < n:
                    
            if prices[r] > prices[l]:
                res += prices[r] - prices[l]

            l = r
            r = l + 1
                
        return res
