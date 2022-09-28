class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Time O(log_4 n)
        # Space O(1)
        k = 0
        while 4 ** k  < n:
            k += 1
        
        return 4 ** k == n
