class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        
        """
        TLE
        
        Time O(n^3)
        
        """
#         self.max_sum = 0 
#         self.res = []

#         def dfs(i, count, val, path):
#             if count == 3:
#                 if val == self.max_sum:
#                     self.res.append(path)
#                 elif val > self.max_sum:
#                     self.max_sum = val
#                     self.res = [path]
#                 return
#             if i >= len(nums): # but count != 3
#                 return 
#             for j in range(i, len(nums)-k+1):
#                 dfs(j+k, count+1, val + sum(nums[j:j+k]), path+[j])
            
#         dfs(0, 0, 0, [])
#         return sorted(self.res)[0]

        """
        DFS with memorization
        
        For each subsequence, dfs on both to take or not to take
        
        Time O(n^2)
        
        """
#         memo = {}
#         def dfs(i, count):
#             if count == 3: # we can only have 3 windows at a time
#                 return 0, []

#             if i >= len(nums):
#                 return 0, []

#             if (i, count) in memo:
#                 return memo[(i, count)]

#             take_sum, take_indices = dfs(i + k, count + 1) # to take
#             take_sum += sum(nums[i:i + k])

#             skip_sum, skip_indices = dfs(i + 1, count)    # or not to take

#             if take_sum >= skip_sum:
#                 memo[(i, count)] = (take_sum, [i] + take_indices)
#                 return memo[(i, count)]
#             else:
#                 memo[(i, count)] = (skip_sum, skip_indices)
#                 return memo[(i, count)]
            
#         res = dfs(0, 0)
#         return res[1]


        """
        3 Sliding Windows Simoutaneously
        
        Time O(n)
        
        """
        bestOneIndex = [0]
        bestTwoIndex = [0, k]
        bestThreeIndex = [0, k, 2*k]
        
        maxOneTotalSum = sum(nums[:k])
        maxTwoTotalSum = sum(nums[:2*k])
        maxThreeTotalSum = sum(nums[:3*k])
        
        curOneSum = sum(nums[:k])
        curTwoSum = sum(nums[k:2*k])
        curThreeSum = sum(nums[2*k:3*k])
        
        n = len(nums)
        for i in range(1, n-k*3+1):
            # remove old num, add new num to window
            curOneSum = curOneSum - nums[i-1] + nums[i+k-1]
            curTwoSum = curTwoSum - nums[i+k-1] + nums[i+2*k-1]
            curThreeSum = curThreeSum - nums[i+2*k -1] + nums[i+3*k-1]
            
            if curOneSum > maxOneTotalSum:
                bestOneIndex = [i]
                maxOneTotalSum = curOneSum
                
            # a better curOneSum might not mean a better curTwoSum
            if curTwoSum + maxOneTotalSum > maxTwoTotalSum: 
                bestTwoIndex = bestOneIndex + [i+k]
                maxTwoTotalSum = curTwoSum + maxOneTotalSum
                
            # a better curTwoSum might not mean a better curThreeSum
            if curThreeSum + maxTwoTotalSum > maxThreeTotalSum:
                bestThreeIndex = bestTwoIndex + [i+2*k]
                maxThreeTotalSum = curThreeSum + maxTwoTotalSum
                
        return bestThreeIndex
        
