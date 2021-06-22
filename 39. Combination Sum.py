class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Searching: DFS
        
        """
        
        res = []
        candidates.sort()
        
        def dfs(target, index, path):
            if target < 0:
                # backtracking
                # failed attempt
                return  
            if target == 0:
                # path works!
                res.append(path)
                return 
            for i in range(index, len(candidates)):
                """
                try all possible (path, [candidates[i]])
                [] [2]
                [2] [2]
                [2, 2] [2]
                [2, 2, 2] [2]
                [2, 2, 2] [3]
                [2, 2, 2] [6]
                ...
                [3] [7]
                [] [6]
                [6] [6]
                [6] [7]
                [] [7]
                """
                dfs(target-candidates[i], i, path+[candidates[i]])
        
        dfs(target, 0, [])
        return res
