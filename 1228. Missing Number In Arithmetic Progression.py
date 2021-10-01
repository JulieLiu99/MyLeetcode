class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        """
        Math
        
        Time O(n)
        Space O(n)
        
        """
        # return ((min(arr) + max(arr)) * (len(arr) + 1) // 2) - sum(arr)
        
        """
        Binary Search
        
        Time O(logn)
        Space O(1)
        
        """
        d = (arr[-1] - arr[0]) // len(arr) 
        l = -1
        r = len(arr)
        
        while l + 1 != r:
            m = l + (r-l)//2
            if arr[m] == arr[0] + d * m: # up to m is valid
                l = m
            else:
                r = m
              
        # l is the last valid num
        return arr[l] + d
