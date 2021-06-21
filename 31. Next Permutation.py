class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Search by pointers
        Thinking through heights
        Try not to touch front part -> so that we find only the next larger nums
        
        1) Swap the last "ascending" position with the last num bigger than it
        2) Make nums from last peak onwards ascending
        
        1 2 3      1 3 2
            /        /\
          /         /  \
        /          /

                    l r       nums
                        [1, 3, 5, 2, 8, 4]
                                  ^ last ascending
        after 1)    4 5 [1, 3, 5, 4, 8, 2]
                                     ^ last peak 
        after 2)    5 4 [1, 3, 5, 4, 2, 8]
        
        Time O(n)
        Space O(1)
        
        """
        
        i = j = len(nums)-1
        
        # find the last peak of position i 
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
         
        # nums are in descending order -> already largest arrangement
        if i == 0:
            nums.reverse()
            return 
        
        k = i - 1   # k is the last "ascending" position 
        
        # find the last j such that its value bigger than the last "ascending" position 
        while nums[j] <= nums[k]:
            j -= 1
        # swap to make the bigger value the last "ascending" position 
        nums[k], nums[j] = nums[j], nums[k]  
        
        # since nums is descending from last peak onwards
        # reverse second part to get smallest nums among the greater arrangements
        l = i
        r = len(nums)-1  
        
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1 
            r -= 1
        
        
