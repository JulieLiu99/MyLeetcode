class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        """
        Recursive DFS
        
        Each row one and only one queen
        Each column one and only one queen
        Each diagnal line one and only one queen
        
        num is a size n list representing positions of queens
        num[row] = col
        
        Fill in the queens row by row, until all rows are filled
        For each row, check all columns to find good position
        For each check, make sure same diagonal line and column not taken
        
        Time O(n^2)
        Space O(n^2)
        
        """
        # check whether nth row queen can be placed in that column
        def valid(row):
            # check diagonal line and column not taken by previous queens in any rows
            for pre_row in range(row):
                if nums[pre_row] == nums[row] or abs(nums[row] - nums[pre_row]) == row - pre_row:
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
                if row == 0:
                    dfs(row + 1, path + ["." * col + "Q" + "." * (n-col-1)])
                elif valid(row):  # pruning
                    dfs(row + 1, path + ["." * col + "Q" + "." * (n-col-1)])
        
        res = []
        nums = [-1]*n
        dfs(0, [])
        return res
