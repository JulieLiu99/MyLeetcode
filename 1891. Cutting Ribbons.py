class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        """
        Binary Search
        
        k ribbons of all the same positive integer length
        
        Return the maximum possible positive integer length that you can obtain k ribbons of
        
        0 if you cannot obtain k ribbons of the same length
        
        Time O(nlogm): search through 0 -10**5 is O(logm), each validation goes through all ribons O(n)
        Space O(1)
        
        """
        l, r = 0, 10**5+1
        while l + 1 != r: 
            same_length = l + (r-l)//2
            if sum(ribbon//same_length for ribbon in ribbons) < k: 
                r = same_length
            else: 
                l = same_length
        return l 
