class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        DFS + memorization
        
        Time O(nlogn + n^2)
        Space O(n + n^2)
        
        """
        
        nums.sort()
        res = []
        n = len(nums)
        used = [False for _ in range(n)]
        
        def dfs(i, path):
            res.append(path)
            for i in range(i, n):
                if i>0 and nums[i] == nums[i-1] and used[i-1] != True:
                    continue
                else:
                    used[i] = True
                    dfs(i+1, path+[nums[i]])
                    used[i] = False
            return
                
        dfs(0, [])
        return res
