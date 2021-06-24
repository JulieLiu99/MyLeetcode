class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Basic idea:
         
        1. For any array whose length is n, the first missing positive must be in range [1,...,len(nums)+1], 
            so we only have to care about those elements in this range and remove the rest.
        2. Use the array index [0,...,len(nums)] as the hash to restore the existence of numbers within 
             the range [1,...,len(nums)+1]. 
           Mark nums[abs(num)-1] as negative if num exists and within range. 
           
        3. Traverse list to find smallest positive number, index + 1 is its value
        
        Time O(n): O(3n) precisely
        Space O(1)
        
           [3,-3, 6, 3]
               ^
      ignore non positive
      
        -> [3, 0, 6, 3]
            ^
         index=2, mark as negative
         
        -> [3, 0,-6, 3]
        
        """
        n = len(nums)
        
        # ignore non positive elements
        for i, num in enumerate(nums):
            if num <= 0:
                nums[i] = 0

        # mark values within range [1,...,len(nums)+1]
        for i, num in enumerate(nums):
            index = abs(num)-1
            if 0 <= index < len(nums):
                if nums[index] == 0:
                    nums[index] = -inf
                elif nums[index] > 0: # we dont want to make negative to be positive again, when its duplicated num
                    nums[index] *= -1

        # locate smallest positive that never showed up
        for index, num in enumerate(nums):
            if num >= 0:
                return index + 1

        return len(nums) + 1
