class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Sliding Window - Two Pointers
         
        -> find max consecutive ones + zeros, such that zero < k
        
        Time O(n)
        Space O(1)
        
        """
        i = j = 0
        max_window = 0
        zeros = 0
        
        while i <= j < len(nums): # check window nums[i~j] = nums[i:j+1]
            
            if nums[j] == 0:
                zeros += 1
                
            if zeros > k:  # if too many 0's, shrink from left side till window is valid
                while zeros > k:
                    if nums[i] == 0: zeros -= 1
                    i += 1
                
            max_window = max(max_window, j-i+1)
                
            j += 1
            
        return max_window
    
        """
        A trick:
        
        No meed to keep max window size
        Whenever there are extra 0's in the window, reduce window size from left side (adjust number of 0's in window if applicable)
        Return final window size in the end
        
        1, 1, 1, 1, 0, 0, 0, 1, 1, k = 2
        ^  ^  ^  ^  ^  ^
        should return 1，1，1，1
        
        1, 1, 1, 1, 0, 0, 0, 1, 1
           ^  ^  ^  ^  ^  ^
        when window gets here, 1 extra 0, shrink window from left, to retain max valid window size

        """
#         l = 0
#         zeros = 0
        
#         for r in range(len(nums)):
#             if nums[r] == 0:
#                 zeros += 1 
            
#             if zeros > k:  # too many 0's in window, move left pointer right by 1
#                 if nums[l] == 0:
#                     zeros -= 1
#                 l += 1

#         return r - l + 1
