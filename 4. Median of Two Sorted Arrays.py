class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Binary search 
        because the overall run time complexity should be O(log (m+n))
        
        Find the middle points in nums1 and nums2, called m1 and m2
        Median has to be from {nums1[m1-1], nums2[m2-1], nums1[m1], nums2[m2]}
        
        Binary search to find m1 of the shorter list
        based on nums1[m1] <? nums2[m2-1]
        m2 = (n1+n2+1)//2 - m1
        
        max_of_left = max(nums1[m1-1], nums2[m2-1])
        min_of_right = min(nums1[m1], nums2[m2])
        
        If odd, return max_of_left
        If even, return (max_of_left + min_of_right) / 2.0
        """
        
        n1, n2 = len(nums1), len(nums2)       # binary search on the shorter list
        if n1 > n2:
            nums1, nums2, n1, n2 = nums2, nums1, n2, n1

        l, r = 0, n1
        half_len = (n1 + n2 + 1) // 2
        
        while l < r:
            m1 = (l + r) // 2       # middle point in nums1
            m2 = half_len - m1          # middle point in nums2
            if nums1[m1] < nums2[m2-1]: 
                l = m1 + 1              # m1 too small, increase it
            else:                       
                r = m1                  # m1 too big, decrease it
                
        m1 = l
        m2 = half_len - l

        if m1 == 0: 
            max_of_left = nums2[m2-1]
        elif m2 == 0: 
            max_of_left = nums1[m1-1]
        else: 
            max_of_left = max(nums1[m1-1], nums2[m2-1])

        if (n1 + n2) % 2 == 1:        # odd number of values
            return max_of_left

        if m1 == n1:                  # even number of values
            min_of_right = nums2[m2]
        elif m2 == n2: 
            min_of_right = nums1[m1]
        else: 
            min_of_right = min(nums1[m1], nums2[m2])

        return (max_of_left + min_of_right) / 2.0
