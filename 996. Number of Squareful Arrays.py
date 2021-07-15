class Solution:

    def numSquarefulPerms(self, nums: List[int]) -> int:
        """
        DFS
        
        Time O(n!)
        Space O(n!)
        
        """
        
        self.res = set()
        n = len(nums)
        
        def dfs(nums, i, path):
            
            if i == n:
                self.res.add(tuple(path))
                return
            
            for j in range(len(nums)):
                
                # need to handle duplicate cases!!! otherwise TLE
                if j > 0 and nums[j] == nums[j-1]: continue
                    
                if not path or math.sqrt(path[-1] + nums[j]) == int(math.sqrt(path[-1] + nums[j])):
                    dfs(nums[:j]+nums[j+1:], i+1, path+[nums[j]])
        
        
        dfs(nums, 0, [])
        return len(self.res)
