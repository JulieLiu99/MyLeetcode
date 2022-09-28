class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Time O(logn)
        # Space O(1)
        k = 0
        while 2 ** k  < n:
            k += 1
        
        return 2 ** k == n
