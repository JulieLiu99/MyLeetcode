class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Iterative
        
        Instead of multiplying by x each time, squre it: x*x, n/2
        
        Time O(logn)
        Space O(1)
        
        """
        # x^(-n) = (1/x)^n
        if n < 0:
            x = 1 / x
            n = -n
            
        power = 1
        
        while n:
            if n & 1:   # n is odd
                power *= x
            x *= x
            n >>= 1     # n/2
            
        return power
    
        """
        Recursive 
        
        Time O(logn)
        Space O(logn)
        
        """
#         if not n:
#             return 1
        
#         if n < 0:
#             return 1 / self.myPow(x, -n)
        
#         if n % 2:
#             return x * self.myPow(x, n-1)
        
#         return self.myPow(x*x, n/2)
