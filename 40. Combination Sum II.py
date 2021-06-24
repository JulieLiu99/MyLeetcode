class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Backtracking
        
        """
        res  = []
        candidates.sort()
        
        def combination(candidates, target, i, path):
            if target == 0:
                res.append(path)
                return
            elif target < 0:
                return
            else:
                for i in range(i, len(candidates)):
                    # skip if same value as previous candidate for this current position
                    if i > 0 and candidates[i] == candidates[i-1]:
                        continue
                    # stop if candidates from now on are too large
                    if candidates[i] > target:
                        break
                    combination(candidates[:i]+candidates[i+1:], target-candidates[i], i, path+[candidates[i]])
                        
        combination(candidates, target, 0, [])

        return res
