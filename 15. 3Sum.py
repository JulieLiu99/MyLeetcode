class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        """
        For each nums[i], find 2sum that equals target-nums[i]
        Time O(nlogn + n^2): sort, one for loop + one while loop
        Space depends on sorting algorithm, otherwise O(1)
        """
        
#         nums.sort()
        
#         n, result = len(nums), []
        
#         for i in range(n-2):
            
#             if i > 0 and nums[i] == nums[i-1]: # skip duplicates
#                 continue
                
#             target = 0 - nums[i]
#             l, r = i+1, n-1
            
#             while l < r:
#                 if nums[l] + nums[r] == target:
#                     result.append([nums[i], nums[l], nums[r]])
#                     l += 1
#                     r -= 1
#                     while l < r and nums[l] == nums[l-1]:
#                         l += 1
#                 elif nums[l] + nums[r] < target:
#                     l += 1
#                 else:
#                     r -= 1
                    
#         return result

        n = len(nums)
        res = set()
        target = 0
        
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]: # skip duplicates
                continue
                
            two_sum = {} # num: i
            for j in range(i+1, n):
                if target - nums[i] - nums[j] in two_sum:
                    res.add(tuple(sorted([nums[i], nums[j], target - nums[i] - nums[j]])))
                else:
                    two_sum[nums[j]] = i
                    
        return list(res)
