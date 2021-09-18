class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Sliding window
         
        -> find max consecutive ones + zeros, such that zero < k
        
        Time O(n)
        Space O(1)
        
        """
        
        l = 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1 # use one allowance
            
            if k < 0:  # allowance all used, move left pointer right
                if nums[l] == 0:
                    k += 1
                l += 1

        return r - l + 1
