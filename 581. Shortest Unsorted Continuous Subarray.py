class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        Two Pointers
        
        Traverse the array twice:
        1. Going forward, find largest index not in place.
        2. Going backward, find the smallest index not in place.
        
        Time O(n) 2 Loops 
        Space O(1) 
        
        """
        if len(nums) <2:
            return 0
        
        prev = nums[0]
        r = 0
		# find the largest index not in place
        for i in range(0, len(nums)):
            if nums[i] < prev:
                r = i
            else:
                prev = nums[i]
        if r == 0: return 0

        l = len(nums) - 1
        prev = nums[l]
		# find the smallest index not in place
        for i in range(len(nums)-1, -1, -1):
            if prev < nums[i]:
                l = i
            else:
                prev = nums[i]
                
        return r - l + 1
