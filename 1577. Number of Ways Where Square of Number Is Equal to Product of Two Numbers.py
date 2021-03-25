class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        
        """
        Time O(n^2)
        Space O(n)
        
        """
        
        d1 = collections.defaultdict(int)
        d2 = collections.defaultdict(int)
        
        for i in nums1:
            d1[i * i] += 1
        for i in nums2:
            d2[i * i] += 1
            
        res = 0
        
        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                multip = nums1[i] * nums1[j]
                if multip in d2:
                    res += d2[multip]
                    
        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                multip = nums2[i] * nums2[j]
                if multip in d1:
                    res += d1[multip]
                    
        return res
