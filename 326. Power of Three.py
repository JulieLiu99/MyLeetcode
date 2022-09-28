class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Time O(log_3 n)
        # Space O(1)
        k = 0
        while 3 ** k  < n:
            k += 1
        
        return 3 ** k == n
            
