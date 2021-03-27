class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        """
        Two Pointers
        Always take the step in the smaller element

        If two elements are the same,
        Compare the accumulated sum in the both paths,
        and pick the bigger one.

        Time O(N)
        Space O(1)
        
        """
        
        i, j = 0, 0     # two pointers
        n, m = len(nums1), len(nums2)
        
        sum1, sum2 = 0, 0     # sum from each path
        mod = 10**9 + 7
        
        while i < n or j < m:
            
            if j == m:
                sum1 += nums1[i]
                i += 1
                
            elif i == n:
                sum2 += nums2[j]
                j += 1
                
            elif nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
                
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
                
            else:   # nums1[i] = nums2[j]
                sum1 = sum2 = max(sum1, sum2) + nums1[i]
                i += 1
                j += 1
                
        return max(sum1, sum2) % mod
