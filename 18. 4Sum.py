class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        """
        Recursion to reduce the N-sum to 2-sum
        Time O(n^3), k-2 loops over n elements, twoSum is O(n)
        Space O(n) for recursion
        """
        
#         def findNsum(l, r, target, N, result, results):

#             # early termination
#             if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N: 
#                 return

#             # two pointers solve sorted 2-sum problem
#             if N == 2: 
#                 while l < r:
#                     s = nums[l] + nums[r]
#                     if s == target:
#                         results.append(result + [nums[l], nums[r]])
#                         l += 1
#                         while l < r and nums[l] == nums[l-1]:
#                             l += 1
#                     elif s < target:
#                         l += 1
#                     else:
#                         r -= 1

#             # recursively reduce N
#             else: 
#                 for i in range(l, r+1):
#                     if i == l or (i > l and nums[i-1] != nums[i]):
#                         findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)
        
#         nums.sort()
#         results = []
#         findNsum(0, len(nums)-1, target, 4, [], results)
#         return results
    

        """
        For each two nums, find 2sum that equals target-nums[i]-nums[j]
        
        Time O(n^3)
        
        """

        n = len(nums)
        res = set()
        explored = set()
        
        for i in range(n-1):
            for j in range(i+1, n-2):
                if (nums[i], nums[j]) in explored: # skip duplicate starts
                    continue
                explored.add((nums[i], nums[j]))
                explored.add((nums[j], nums[i]))
                
                two_sum = set()
                for k in range(j+1, n):
                    if target - nums[i] - nums[j] - nums[k] in two_sum:
                        res.add(tuple(sorted([nums[i], nums[j], nums[k], target - nums[i] - nums[j] - nums[k]])))
                    else:
                        two_sum.add(nums[k])
                    
        return list(res)
