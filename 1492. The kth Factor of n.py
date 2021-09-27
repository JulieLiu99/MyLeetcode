class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        """
        Time: O(n)
        Space: O(1)
        
        """
        # for factor in range(1, n + 1):
        #     if n % factor == 0:
        #         k -= 1
        #         if k == 0:
        #             return factor
        # return -1
        
        """
        Time: O(n ^ 0.5)
        Space: O(1)
        
        """
        isqrt = math.isqrt(n)
        
        for i in range(1, isqrt + 1):
            if n % i == 0:
                k -= 1
                if k == 0: return i
                
        for i in reversed(range(1, isqrt + 1)):
            if i * i == n: continue
            if n % i == 0:
                k -= 1
                if k == 0: return n // i
                
        return -1
