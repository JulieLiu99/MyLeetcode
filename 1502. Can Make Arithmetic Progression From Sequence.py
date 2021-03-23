class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        """
        Most intuitive: sort + traverse
        
        Time O(nlogn), but actually faster than the other solution
        Space O(1)
        
        """
        s = sorted(arr)
        diff = s[1] - s[0]
        for i in range(2, len(s)):
            if diff != s[i] - s[i-1]:
                return False
        return True
        
        
        """
        Find gap by dividing distance between minimun and maximun number.
        Check all numbers are evenly distributed.

        Time: O(N)
        Space: O(1) because we do it in place

        """
        """
        m = min(arr)
        diff = (max(arr) - m) / (len(arr) - 1)
        if diff == 0: return True
        i = 0
        while i < len(arr):
            gap = arr[i] - m
            if gap == i * diff:
                i += 1
            else:
                if gap % diff != 0: return False
                pos = int(gap / diff)
                if arr[pos] == arr[i]: return False
                arr[pos], arr[i] = arr[i], arr[pos]
        return True
        """


