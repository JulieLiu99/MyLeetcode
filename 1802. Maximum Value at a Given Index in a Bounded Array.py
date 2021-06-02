class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        """
        Binary Search
        
        Time O(log(maxSum))
        Space O(1)
        
        """
        # To check for a given number x, greedily minimize the array's sum.
        # First, place the number at the index. 
        # Then, on both the left and right side, start counting down from that number. 
        # E.g. with n = 7, index = 4, to place a 10, our optimal array would look like: 
        # [6, 7, 8, 9, *10, 9, 8]. 
        #  0  1  2  3   4   5  6
        # To do the calculations, use the partial sums of this infinite series.

        def test(x):
            # number of elements on the left
            if index > x-1:
                # [1, 1, 1, *2, 1]
                #  0  1  2   3  4
                left = x * (x - 1) / 2 + (index - (x - 1))
            else:
                left = (x - 1 + x - index) * index / 2
                
            # number of elements on the right
            if n - index - 1 > x - 1:
                # [1, *2, 1, 1]
                #  0   1  2  3 
                right = x * (x - 1) / 2 + (n - index - 1 - (x - 1))
            else:
                right = (x - 1 + x - (n - index - 1)) * (n - index - 1)  / 2 
                
            return left + x + right 
        
        # find min x such that test(x) > maxSum, return (x-1)
        l = 1
        r = maxSum + 1
        
        while l < r:
            m = l + (r - l) // 2
            if test(m) <= maxSum:
                l = m + 1
            else:
                r = m 
                
        return l - 1
