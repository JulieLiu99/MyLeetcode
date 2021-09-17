class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        """
        Traverse the list, compare adjacent elements
        If not continuous, 
            if differ by 2, res.append(str(num1+1))
            else res.append(str(num1+1) + "->" + str(num2-1))
        
        Time O(n)
        Space O(1)
        
        """
        res = []
        
        if not nums: 
            if lower == upper:
                return [str(lower)]
            else:
                return [str(lower) + "->" + str(upper)]
        
        if nums[0] > lower:
            if lower + 1 == nums[0]:
                res.append(str(lower))
            else:
                res.append(str(lower) + "->" + str(nums[0]-1))
        
        for i in range(1, len(nums)):
            if nums[i-1] + 1 == nums[i]:
                continue
            elif nums[i-1] + 2 == nums[i]:
                res.append(str(nums[i-1]+1))
            else:
                res.append(str(nums[i-1]+1) + "->" + str(nums[i]-1))
                
        if nums[-1] < upper:
            if nums[-1] + 1 == upper:
                res.append(str(upper))
            else:
                res.append(str(nums[-1]+1) + "->" + str(upper))
        
        return res
