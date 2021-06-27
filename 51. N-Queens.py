class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        """
        Recursive DFS
        
        Time O(n^2)
        Space O(n^2)
        
        """
        
        res = []
        self.dfs([-1]*n, 0, [], res)
        return res

    # nums is a one-dimension array, like [1, 3, 0, 2] means
    # first queen is placed in column 1, second queen is placed
    # in column 3, etc.
    def dfs(self, nums, index, path, res):
        if index == len(nums):
            res.append(path)
            return  # backtracking
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):  # pruning
                tmp = "."*len(nums)
                self.dfs(nums, index+1, path+[tmp[:i]+"Q"+tmp[i+1:]], res)

    # check whether nth queen can be placed in that column
    def valid(self, nums, index):
        for i in range(index):
            # if distance between nums[i] and nums[index] equals distance between index and i, the two points must be vertices of a square and must be in same diagonal
            if abs(nums[i]-nums[index]) == index -i or nums[i] == nums[index]:
                return False
        return True
