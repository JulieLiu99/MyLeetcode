class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        """
        Bucket sort: two pass
        
        First pass get count for each. Second pass modify nums.
        Time O(n)
        Space O(1)
        
        """
        # counter = Counter(nums)
        # i = 0
        # for val in [0, 1, 2]:
        #     nums[i: i+counter[val]] = [val] * counter[val]
        #     i += counter[val]
            
        """
        Quick sort: one pass
        
        Three pointers - one for 0 on the left, one for 2 on the right, one for i to be swapped.
        If nums[i] is 0, swap to front; if nums[i] is 2, swap to back.
        Time O(n)
        Space O(1)
    
        [2,0,2,1,1,0]
         ^         ^
         ^
        [0,2,2,1,1,0]
           ^       ^
           ^
        [0,0,2,1,1,2]
           ^     ^
           ^
        [0,0,2,1,1,2]
             ^   ^
             ^
        [0,0,1,1,2,2]
             ^ ^
             ^
        [0,0,1,1,2,2]
             ^ ^
               ^      
        
        [2,0,1]
         ^   ^
         ^
        [1,0,2]
         ^ ^
         ^
        [1,0,2]
         ^ ^
           ^
        [0,1,2]
         ^ ^
             ^
        """
        l = 0
        r = len(nums) - 1
        i = 0
        
        while i <= r: # when i == r, i might still needs to be swapped to front
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                # not updating i in case now nums[i] is 2, which also needs be swapped back
            else:
                i += 1
