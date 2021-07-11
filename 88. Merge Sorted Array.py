class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        Two pointers, while loop
        
        Increment i if nums1[i] is smaller or equal
        Insert when nums2[j] is bigger
        Before insert, shift nums1 from i+1 onwards back
        
        Time O(n)
        Space O(1)
        
        """
        
        if n == 0: 
            return  # m as it is
        
        if m == 0: 
            nums1[:] = nums2[:]
            return 
                
        i = 0
        j = 0
        
        # m+j+1 is the length of nums1 plus num2 inserted into nums1
        while i < m+j+1 and j < n:
        
            if nums1[i] <= nums2[j]:
                i += 1
              
            # [1,2,3,0,0,0] 
            #      ^
            # [2,5,6]
            #  ^
            # [1,2,2,3,0,0] 
            #        ^
            # [-,5,6]
            #    ^
            else:
                nums1[i+1:] = nums1[i:m+n-1]    # shift nums1 from i+1 onwards back
                nums1[i] = nums2[j]
                i += 1
                j += 1
                
        if j < n:   # nums2 left
            nums1[-(n-j):] = nums2[j:]
