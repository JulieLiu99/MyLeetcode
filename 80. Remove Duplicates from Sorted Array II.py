class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        
        While loop
        
        Replace subarray starting from first excessive value 
        with subarray starting from the next different value
        or [] if at end
        
        Time O(n)
        Space O(1)
        
        """
        
        cur = nums[0]
        count = 1
        i = 1
        
        while i < len(nums):
            
            if nums[i] == cur:
                count += 1
            else:
                cur = nums[i]
                count = 1
                
            if count > 2:   # nums[i] to be replaced by next different val
                j = i
                while j < len(nums)-1 and nums[j] == nums[j+1]:
                    j += 1
                if j == len(nums)-1:        # same val till end
                    nums[i:] = []
                    return i    
                else:               # nums[j+1] is new val
                    nums[i:] = nums[j+1:]
                    cur = nums[i]
                    count = 1
            i += 1
            
        return i
