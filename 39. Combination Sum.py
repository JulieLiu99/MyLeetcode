class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        
        def dfs(target, i, path):
            if target < 0:
                return  
            if target == 0:
                res.append(path)
                return 
            for j in range(i, len(candidates)): # can reuse number at i
                dfs(target-candidates[j], j, path+[candidates[j]])
        
        dfs(target, 0, [])
        return res
