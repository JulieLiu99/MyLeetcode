class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        """
        Time O(log^(n)): n is the number of bits
        time goes up linearly while temp goes up exponentially
        Space O(1)
        
        """
        
        negative = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        
        while dividend >= divisor:
            temp, i = divisor, 1    # temp: 1 --> 2 --> 4 --> 16 --> ...
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
                
        if negative:
            res = -res
            res = max(-2147483648, res)
        else:
            res = min(2147483647, res)
            
        return res


