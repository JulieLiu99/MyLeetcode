class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        """
        Iterate through the list
        Collect gaps between consecutive numbers

        Add dummy edges lower-1 and upper+1 to handle edge cases

        Time O(n)
        Space O(1)
        """
        res = []
        prev = lower - 1
        nums.append(upper + 1)
        
        for num in nums:
            if num - prev > 1: # gap
                res.append([prev + 1, num - 1])
            prev = num
        
        return res

