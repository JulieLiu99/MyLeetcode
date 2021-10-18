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
        def cut_into(length):
            return sum(ribbon//length for ribbon in ribbons)
        
        l = 0
        r = 10**5+1
        while l + 1 != r: 
            length = l + (r-l)//2
            if cut_into(length) < k: # need smaller length
                r = length
            else: 
                l = length
        return l 