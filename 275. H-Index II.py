class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        Binary Search

        1. The array is sorted (must be utilized for our solution)
        2. h value is the number where arr[h] == n - h (number of values >=  arr[h])
        3. It is possible to not have an exact h index in arr but in between 2 values
        
        Case 1: If exact h value exist in array, find arr[h] == n - h
        Case 2: If exact h value doesn't exist, find the upper bound of the hindex present in the array and return n - l
        
        Time O(log n) 
        Space O(1)
        
        """
        if not citations: 
            return 0
        n = len(citations)
        l = 0
        r = n - 1
        while l <= r:
            mid = l + (r - l)//2
            if citations[mid] == n - mid:
                return citations[mid]
            elif citations[mid] > n - mid:
                r = mid - 1
            else:
                l = mid + 1                
        return n - l    # maximum h is the number of right hand elements/ citations[l]-1 if l within range
