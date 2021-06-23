class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        
        """
        Two Pointer
        
        check if possible to close the gap between two sums
        
        if possible
        change the element that could close the gap the most
        larger sum list: 6 -> 1; smaller sum list: 1 -> 6
        sort lists to know which element can bring most change
        
        Time O(nlogn + mlogm + (m+n)): sort + two pointer
        Space O(1)
        
        """
        # 6*shorter_list < 1*longer_list -> impossible gap
        if 6*len(nums1) < len(nums2) or 6*len(nums2) < len(nums1): 
            return -1 
        
        if sum(nums1) < sum(nums2): 
            nums1, nums2 = nums2, nums1
            
        s1, s2 = sum(nums1), sum(nums2) # s1 >= s2
            
        # sort both in increasing order, so we know which element to change
        # change the element that could close the gap the most
        # nums1: 6 -> 1; nums2: 1 -> 6
        nums1.sort()
        nums2.sort()
        
        ans = 0
        i = len(nums1)-1  # biggest element in nums1 -> decrease first
        j = 0   # smallest element in nums2 -> increase first
        
        while s1 > s2: 
            # if can't increase nums2 anymore
            # or decrease nums1 is more effective
            if j >= len(nums2) or (i >= 0 and nums1[i] - 1 > 6 - nums2[j]): 
                s1 -= nums1[i] - 1
                i -= 1
            # if can increase nums2
            # and decrease nums1 is not more effective
            else: 
                s2 += 6 - nums2[j]
                j += 1
            ans += 1
        
        # after the last operation from s1 > s2 to s1 <= s2
        return ans 
