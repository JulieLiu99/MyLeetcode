class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        Divide two integers without using 
            multiplication, 
            division, 
            and mod operator.
        
        Division --can be converted to--> Deletion (from dividend delete divisor)
        
        Optimization: We want to delete as few times as possible
        -> Increase the divisor, by *2 (or left shift) 
        12 / 3 = 4
           / 6 = 2 (each divisor 6 divides twice as much as 3)
           
        -> Increase the result by the number of *2 (or left shift) applied to divisor
        
        Time (log2(dividend/divisor))
    
        """
        
        MIN_VAL = -2**31
        MAX_VAL = 2**31 - 1
        
        # edge case when divisor = 1/-1
        if divisor == 1:
            if dividend < MIN_VAL or dividend > MAX_VAL:
                return 2**31 - 1
            else:
                return dividend
        elif divisor == -1:
            if -dividend < MIN_VAL or -dividend > MAX_VAL:
                return 2**31 - 1
            else:
                return -dividend
            
        sign = -1 if (dividend < 0 and divisor > 0) or (divisor < 0 and dividend > 0) else 1
        
        dividend = abs(dividend) 
        divisor = abs(divisor) 
    
        res = 0 
        shift = 31 # at most 31 left shift can be done on a integer value 
        while dividend >= divisor: # if dividend < divisor, truncate towards 0
            
            while dividend < (divisor << shift): # decrease divisor so it maximumly reaches the dividend
                shift -= 1
                
            dividend -= divisor << shift # subtract the left shifted divisor
            res += 1 << shift # left shift 1 by shifts used for divisor
            
        if sign == -1: res = -res   
        if res < MIN_VAL or res > MAX_VAL:
            return 2**31 - 1
        else:
            return res

