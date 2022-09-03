class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        Set first row at the end because we are using it as marker
        Can't set it all zeros immediately
        
        Same for first column
        
        Time O(mn)
        Space O(1)
        
        """
        m = len(matrix)
        n = len(matrix[0])
		
        first_row_has_zero = False
        first_col_has_zero = False
        
        # use first row/col as marker for zero row/col
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_row_has_zero = True
                    if col == 0:
                        first_col_has_zero = True
                    matrix[row][0] = matrix[0][col] = 0
    
        # set cell to zero if it's in a zero row/col
        for row in range(1, m):
            for col in range(1, n):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        
        # update first row and col if they have zero
        if first_row_has_zero:
            matrix[0] = [0] * n
        
        if first_col_has_zero:
            for row in range(m):
                matrix[row][0] = 0


        """
        Don't set neighboring cells to 0s yet
        Because that might have ripple effect
        
        We only want ripple effect from original 0s
        Set to "a" instead, meaning it's in a zero row/col
        
        In the end set all "a"'s to 0s
        
        Time O(mn * (m+n))
        Space O(1)
        
        """

#         n = len(matrix)
#         m = len(matrix[0])
#         if m == 0 or n == 0: return
        
#         for i in range(n):
#             for j in range(m):
#                 if matrix[i][j] == 0:
#                     for _ in range(n):
#                         if matrix[_][j] != 0:
#                             matrix[_][j] = 'a'
#                     for _ in range(m):
#                         if matrix[i][_] != 0: 
#                             matrix[i][_] = 'a'

#         for i in range(n):
#             for j in range(m):
#                 if matrix[i][j] == 'a':
#                     matrix[i][j] = 0
