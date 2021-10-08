class Solution:
    def findMedianSortedArrays(self, A, B):
        """
        Reduce find median to find k-th in two arrays, where k = n/2
        
        Each time reduce search space by half (but include the middle points)
        
        Time O(log(min(m,n)): binary seach for splitting point on smaller array. if smaller array all discarded, then get remainning k-th from larger one
        Space O(1)
        
        """
        n = len(A) + len(B)
        if n % 2 == 1: # 5 elements -> index 2
            return self.findKth(A, B, n//2)  
        else: # 4 elements -> index 1 and 2
            return (self.findKth(A, B, n//2-1) + self.findKth(A, B, n//2)) / 2 
            
            
    def findKth(self, A, B, k):
        
        if len(A) > len(B): # make A the smaller one
            A, B = B, A
            
        if not A:
            return B[k]
        
        if k == len(A) + len(B) - 1:
            return max(A[-1], B[-1])

        i = min(len(A)-1, k//2)
        j = k-i

        if A[i] > B[j]:
            return self.findKth(A[:i], B[j:], k-j) # B[:j] for sure smaller than half of all elements
        else:
            return self.findKth(A[i:], B[:j], k-i) # A[:i] for sure smaller than half of all elements


