class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Edge case: 
            If x is smaller than arr[0] or larger than arr[-1], 
            Return the subarray at the corresponding end
        
        Binary search:
            Find position of x in arr, 
            Go from there to left/right (depending one which side is closer) using two pointers, 
            Return the neighboring subarray
            
            
        Time O(logn + k) runs very fast
        Space O(1)
            
        [1,2,3,4,5]
             ^j
        """
        r = bisect_left(arr, x) # first i such that arr[i] >= x
        l = r 

        while r - l < k: # window arr[l:r], expand from center
            if l == 0:
                r += 1
                continue
            
            if r == len(arr):
                l -= 1
                continue
                
            if abs(arr[l-1] - x) <= abs(arr[r] - x):
                l -= 1
            else:
                r += 1
        
        return arr[l:r]

        """
        Instead of going from value closest to x in the middle of arr
        Go from two ends and move two pointers to the middle
        
        Time O(n-k)
        Space O(1)
        
        """
#         i = 0
#         j = len(arr) - 1
        
#         while j-i+1 != k: # arr[i~j]
#             if x - arr[i] > arr[j] - x:
#                 i += 1
#             else:
#                 j -= 1
        
#         return arr[i:j+1]
        
