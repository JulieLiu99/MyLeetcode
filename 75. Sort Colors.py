class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        Time O(n): l travels n, r travels O(3n)
        Space O(1)
        
        """
        n = len(nums)
        if n in [0, 1]: return 
        
        l = 0
        r = 1
        
        for val in [0, 1, 2]:
            while r <= n-1:
                if nums[l] == val:
                    l += 1
                    r += 1
                elif nums[r] == val: # nums[l] != val
                    nums[l], nums[r] = nums[r], nums[l] # switch
                    l += 1
                    r += 1
                else: # both != val
                    r += 1
                    
            if l == n-1: return # entire list sorted
            r = l + 1
