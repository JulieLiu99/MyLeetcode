class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Bruteforce: At each step,  3 options. O(3^n)

        DP: State machine. O(n)

        hold[i] = max(hold[i-1], rest[i-1] - prices[i])
        sold[i] = hold[i-1] + prices[i]
        rest[i] = max(rest[i-1], sold[i-1])

        init: rest[0] = sold[0] = 0, hold[0] = -inf
        res: max(rest[-1], sold[-1])

        Space: O(n) -> O(1)

        https://www.youtube.com/watch?v=oL6mRyTn56M
        """
        
        sold = 0
        rest = 0
        hold = float('-inf') # cannot hold on first day

        for price in prices:
            prev_sold = sold
            sold = hold + price # from sell
            hold = max(hold, rest - price) # from rest or buy
            rest = max(rest, prev_sold) # from rest or rest after sold

        # why not hold? hold can come from buy or rest
        # if from buy, why buying on the last day
        # if from rest, always better to sell 
        return max(rest, sold)
