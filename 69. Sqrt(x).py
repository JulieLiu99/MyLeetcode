class Solution:
    def mySqrt(self, x: int) -> int:
        
        """
        Linear Search 
        
        O(x): pass but slow
        
        """
        
        # i = 0
        # while i <= x:
        #     if i*i == x:
        #         return i
        #     elif i*i < x:
        #         i += 1
        #     else:  # i*i > x:
        #         return i-1
        
        """
        Binary Search 
        
        O(logx)
        
        """
        
        l = -1
        r = x+1
        while l+1 != r:
            m = l + (r-l)//2
            if m*m == x:
                return m
            elif m*m < x:
                l = m
            else:
                r = m
                
        return l
