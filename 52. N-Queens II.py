class Solution:
    def totalNQueens(self, n: int) -> int:
        
        """
        Use a dictionary to check duplicate
        Add string instead of list into result dictionary
        
        """
#         # check whether nth row queen can be placed in that column
#         def valid(row):
#             # check diagonal line and column not taken by previous queens in any rows
#             for pre_row in range(row):
#                 if nums[pre_row] == nums[row] or abs(nums[row] - nums[pre_row]) == row - pre_row:
#                     return False
#             return True
        
#         # nums is a one-dimension array, like [1, 3, 0, 2] means
#         # first row queen is placed in column 1, second row queen is placed
#         # in column 3, etc.
#         def dfs(row, path):
#             if row == n:
#                 if "".join(path) not in res:
#                     res["".join(path)] = 1
#                     return  # backtracking
#             for col in range(n):
#                 nums[row] = col
#                 if row == 0:
#                     dfs(row + 1, path + ["." * col + "Q" + "." * (n-col-1)])
#                 elif valid(row):  # pruning
#                     dfs(row + 1, path + ["." * col + "Q" + "." * (n-col-1)])
        
#         res = {}
#         nums = [-1]*n
#         dfs(0, [])
#         return len(res)
    
        """
        Have number of solution as a int variable
        Because backtracking goes row by row, and column by column
        Each solution is already distinct
        
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
                self.res += 1
                return  # backtracking
            for col in range(n):
                nums[row] = col
                if row == 0:
                    dfs(row + 1, path + ["." * col + "Q" + "." * (n-col-1)])
                elif valid(row):  # pruning
                    dfs(row + 1, path + ["." * col + "Q" + "." * (n-col-1)])
        
        nums = [-1]*n
        self.res = 0
        dfs(0, [])
        return self.res
