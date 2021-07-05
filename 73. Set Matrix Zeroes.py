class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        Time O(mn)
        Space O(m+n)
        
        Good performance already
        
        """
        
#         rows = set()
#         cols = set()
        
#         n = len(matrix)
#         m = len(matrix[0])
#         if m == 0 or n == 0: return
        
#         for row in range(n):
#             for col in range(m):
#                 if matrix[row][col] == 0:
#                     rows.add(row)
#                     cols.add(col)              
        
#         for row in rows:
#             matrix[row] = [0 for _ in range(m)]
            
#         for col in cols:
#             for row in range(n):
#                 matrix[row][col] = 0
                
                
        """
        'a' means to be turned to 0
        
        Time O(mn)
        Space O(1)
        
        Better memoray use, though slower compared to above
        
        """

        n = len(matrix)
        m = len(matrix[0])
        if m == 0 or n == 0: return
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    for tmp in range(n):
                        if matrix[tmp][j] != 0:
                            matrix[tmp][j] = 'a'
                    for tmp in range(m):
                        if matrix[i][tmp] != 0: 
                            matrix[i][tmp] = 'a'

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 'a':
                    matrix[i][j] = 0
