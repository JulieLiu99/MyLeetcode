class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Sort then count
        
        Time O(nlogn)
        Space O(sort)
        
        """
#         if not nums: return 0
        
#         nums.sort()
#         longest = 0
#         cur_longest = 1
        
#         for i in range(1,len(nums)):
#             if nums[i] - nums[i - 1] == 1: # consecutive 
#                 cur_longest += 1
#             elif nums[i] - nums[i - 1] > 1: # no longer consecutive
#                 longest = max(longest, cur_longest)
#                 cur_longest = 1
                
#         return max(longest, cur_longest)

        """
        Look up in set
        
        Time O(n)
        Space O(n)
        
        """
        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums: # start of consecutive
                count = 1
                while num + count in nums: 
                    count += 1
                longest = max(longest, count)
        return longest
