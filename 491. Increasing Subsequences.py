class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        """
        DFS
        
        Time O(2^n)
        Space O(2^n)
        
        """
        
        self.res = set()
        n = len(nums)
        
        def dfs(i, path):
            if len(path) > 1:
                # tuple because it's hashable, unlike list
                self.res.add(tuple(path[:]))
            
            for j in range(i, n):
                if not path or path[-1] <= nums[j]:
                    dfs(j+1, path+[nums[j]])
        
        dfs(0, [])
        return list(self.res)
