class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Brute Force: Go through the list O(n)
        
        O(logn) time: binary search
        
        Two ends are infinitely deep, just need to return any peak
        
               *
             *
        *  *   *
             ^ if next goes up, peak is on the right
             
        [1,2,1,3,5,6,4]
               ^
                   ^  
        """
        l = -1
        r = len(nums)
        
        while l + 1 != r:
            
            m = l + (r-l)//2
            
            if m+1 < len(nums) and nums[m+1] >= nums[m]:
                l = m
                
            elif m-1 >= 0 and nums[m-1] > nums[m]:
                r = m
                
            else: # neither left nor right is higher than current m
                return m
