class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        """
        One pass: left / right/ middle removal
        
        Time O(n)
        Space O(1)
        
        """

        l, r = 0, len(arr) - 1
        while l < len(arr) - 1 and arr[l+1] >= arr[l]:
            l += 1
        if l == len(arr) - 1: return 0 
        
        while r > 0 and arr[r-1] <= arr[r]:
            r -= 1
        if r == 0: return 0
        
        toRemove = min(len(arr) - l - 1, r)     # one side removal
		
        for iL in range(l+1):                   # middle removal
            if arr[iL] <= arr[r]:
                toRemove = min(toRemove, r - iL - 1)
            elif r < len(arr) - 1:
                r += 1
            else:
                break
        return toRemove
