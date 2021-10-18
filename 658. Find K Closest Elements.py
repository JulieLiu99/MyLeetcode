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
        
#         if x >= arr[-1]: # only take from the end
#             return arr[-k:]
        
#         if x <= arr[0]: # only take from the front
#             return arr[:k]
        
#         j = bisect.bisect_left(arr, x) # arr[j] >= x
#         if j > 0 and arr[j]-x >= x-arr[j-1]: j -= 1 # j has value closest to x
#         i = j-1
        
#         # find arr[i+1 ~ j]
#         while j - i < k and i >= 0 and j + 1 < len(arr):
#             if arr[j+1]-x < x-arr[i]:
#                 j += 1
#             else: # arr[j+1]-x >= x-arr[i]
#                 i -= 1
                
#         if j - i < k and i < 0:  # need more from the end
#             j += k - (j-i) 
            
#         elif j - i < k and j + 1 >= len(arr):  # need more from the front
#             i -= k - (j-i) 
        
#         return arr[i+1:j+1]

        """
        Instead of going from value closest to x in the middle of arr
        Go from two ends and move two pointers to the middle
        
        Time O(n-k)
        Space O(1)
        
        """
    
        i = 0
        j = len(arr) - 1
        
        while j-i+1 != k: # arr[i~j]
            if x - arr[i] > arr[j] - x:
                i += 1
            else:
                j -= 1
        
        return arr[i:j+1]
        
