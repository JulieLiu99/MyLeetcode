class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Two ends of nums will have the largest squres
        -> At the end of the output
        
        Two pointers l and r, initialized at two ends
        Meet at center, smallest absolute value
        
        Time O(n)
        Space O(1)
        """
#         if nums[0] >= 0: # all non negative
#             return [num**2 for num in nums]
        
#         l = 0
#         r = len(nums) - 1
#         res = []
        
#         # <= instead of < because for the last num, l has already += 1 OR r has already -= 1
#         while l <= r: 
#             if abs(nums[l]) < abs(nums[r]):
#                 res.insert(0, nums[r]**2) # insert(index, element)
#                 r -= 1
#             else:
#                 res.insert(0, nums[l]**2) 
#                 l += 1
#         return res


        """
        Reversing res in the end instead of inserting to 0 all the time is faster
        insert() takes O(n) time for each call
        reversed() or [::-1] takes O(n) time
        """
        if nums[0] >= 0: # all non negative
            return [num**2 for num in nums]
        
        l = 0
        r = len(nums) - 1
        res = []
        
        # <= instead of < because for the last num, l has already += 1 OR r has already -= 1
        while l <= r: 
            if abs(nums[l]) < abs(nums[r]):
                res.append(nums[r]**2) 
                r -= 1
            else:
                res.append(nums[l]**2)
                l += 1
                
        return reversed(res)
