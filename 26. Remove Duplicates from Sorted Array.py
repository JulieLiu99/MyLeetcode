class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Two Pointers (newTail and i): [1,1,2] --> [1,2]
        Time O(n)
        Space O(1)
        """
        
        if not nums:
            return 0

        newTail = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]
            
        # remove duplicates
        for j in range(newTail+1, len(nums)):
            nums.pop(-1)

        return newTail + 1
