class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        """
        DFS
        
        Time O(n!)
        Space O(n!)
        
        """
        
        self.res = []
        
        def dfs(nums, path):
            
            if not nums:
                self.res.append(path)
                return # backtracking
            
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], path+[nums[i]])
            
        dfs(nums, [])
        return self.res
