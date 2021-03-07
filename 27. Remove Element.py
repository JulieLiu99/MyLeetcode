class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        """
        Two pointer
        Time O(n)
        Space O(1)
        """
        
        i = 0
        
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
                
        for j in range(i, len(nums)):
            nums.pop(-1)
            
        return i
