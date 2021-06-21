class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        1 2 3      1 3 2
            /        /\
          /         /  \
        /          /
        """
        
        i = j = len(nums)-1
        
        # find the last peak of position i -> to be swapped one position earlier
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
         
        # nums are in descending order -> already largest arrangement
        if i == 0:
            nums.reverse()
            return 
        
        k = i - 1   # the last "ascending" position 
        
        # find the last j such that its value bigger than the last "ascending" position 
        while nums[j] <= nums[k]:
            j -= 1
        # swap to make the bigger value the last "ascending" position 
        nums[k], nums[j] = nums[j], nums[k]  
        
        # since nums is descending from last peak onwards
        # reverse second part to get smallest nums among the greater arrangements
        l = i
        r = len(nums)-1  
        
        """
        l r      nums
            [1, 5, 2, 8, 3]
        3 4 [1, 5, 3, 8, 2]
        4 3 [1, 5, 3, 2, 8]
        """
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1 
            r -= 1
            print(l, r, nums)
