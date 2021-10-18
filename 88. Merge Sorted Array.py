class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        Two pointers
        
        Since in place, gradually appending larger ones of nums1 and nums2 to the end
        If there is any space and nums2 left, put rest of nums2 into the space
        
        Time O(m+n)
        Space O(1)
        
        """
        i = m-1
        j = n-1
        k = m+n-1
        while i >= 0 and j >= 0:
            if nums2[j] >= nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
            
        if j >= 0: # put remaining nums2 into empty space
            nums1[:k+1] = nums2[:k+1]
