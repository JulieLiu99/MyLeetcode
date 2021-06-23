class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        # if later num is same, ignore 
        # bc we've already exhausted all permutations starting from that value
    
        res, visited = [], [False]*len(nums)
        # after sorting, duplicated number will be next to each other
        # this way the duplication check nums[i] == nums[i-1] will work
        nums.sort()

        def dfs(visited, path):
            if len(nums) == len(path):
                res.append(path)
                return 
            for i in range(len(nums)):
                if not visited[i]: 
                    if i>0 and not visited[i-1] and nums[i] == nums[i-1]: 
                        continue
                    visited[i] = True
                    dfs(visited, path+[nums[i]])
                    visited[i] = False

        dfs(visited, [])
        return res
