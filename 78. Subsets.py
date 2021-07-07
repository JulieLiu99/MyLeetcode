class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """       
        Interative
        
        Time O(n)
        Space O(1)
        
        """
        
        res = [[]]
        for num in nums:
            n = len(res)
            for i in range(n):
                res.append(res[i] + [num])
        return res
    
        """       
        Recursive DFS
        
        Time O(n)
        Space O(n)
        
        """
#     def subsets(self, nums):
#         res = []
        
#         def dfs(nums, path):
#             res.append(path)
#             for i in range(len(nums)):
#                 dfs(nums[i+1:], path+[nums[i]])
            
#         dfs(nums, [])
#         return res
