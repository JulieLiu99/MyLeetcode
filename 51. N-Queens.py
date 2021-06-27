class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        """
        Recursive DFS
        
        Time O(n^2)
        Space O(n^2)
        
        """
        # check whether nth row queen can be placed in that column
        def valid(row):
            for pre_row in range(row):
                # if distance between rows equals distance between cols, the two points must be vertices of a square and must be in same diagonal
                if abs(nums[pre_row] - nums[row]) == row - pre_row or nums[pre_row] == nums[row]:
                    return False
            return True
        
        # nums is a one-dimension array, like [1, 3, 0, 2] means
        # first row queen is placed in column 1, second row queen is placed
        # in column 3, etc.
        def dfs(row, path):
            if row == n:
                res.append(path)
                return  # backtracking
            for col in range(n):
                nums[row] = col
                if  valid(row):  # pruning
                    dfs(row + 1, path + ["." * col + "Q" + "." * (n-col-1)])
        
        res = []
        nums = [-1]*n
        dfs(0, [])
        return res
