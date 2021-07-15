class Solution:

    def numSquarefulPerms(self, nums: List[int]) -> int:
        """
        DFS
        
        Time O(n!)
        Space O(n!)
        
        """
        
#         self.res = set()
#         n = len(nums)
        
#         def dfs(nums, i, path):
            
#             if i == n:
#                 self.res.add(tuple(path))
#                 return
            
#             for j in range(len(nums)):
                
#                 # need to handle duplicate cases!!! otherwise TLE
#                 if j > 0 and nums[j] == nums[j-1]: continue
                    
#                 if not path or math.sqrt(path[-1] + nums[j]) == int(math.sqrt(path[-1] + nums[j])):
#                     dfs(nums[:j]+nums[j+1:], i+1, path+[nums[j]])
        
        
#         dfs(nums, 0, [])
#         return len(self.res)

        
        """
        Another way, also works
        
        Use a used list to track used nums
        
        """
        self.res = 0
        n = len(nums)
        nums.sort()
        used = [False for _ in range(n)]
        
        def dfs(i, path):
            
            if i == n:
                self.res += 1
                return
            
            for j in range(n):
                
                if used[j]: continue
                
                if j > 0 and nums[j] == nums[j-1] and not used[j-1]: continue
                    
                if not path or math.sqrt(path[-1] + nums[j]) == int(math.sqrt(path[-1] + nums[j])):
                    used[j] = True
                    dfs(i+1, path+[nums[j]])
                    used[j] = False
        
        dfs(0, [])
        return self.res
