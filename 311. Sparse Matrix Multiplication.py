class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        """
        Result matrix: rows = rows1, cols = cols2, l inner dimension

        Naiive implementation: 
        Time: O(rows * cols * l)
        However, many elements along each l dimension are zeros.
        
        Optimization:
        Traverse mat1's l dimension and record nonzero indices&values.
        Only look at corresponding indices in mat2's l dimension.
        Space: O(nonzero k's)
        Time: O(rows * (l + cols * nonzero k's))
        
        """
        rows = len(mat1)
        cols = len(mat2[0])
        l = len(mat1[0])  # length of one multiplication
        res = [[0 for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):

            # for col in range(cols):
            #     for k in range(l):
            #         res[row][col] += mat1[row][k] * mat2[k][col]

            mat1_nonzero = {}
            for k in range(l):
                if mat1[row][k]:
                    mat1_nonzero[k] = mat1[row][k]
            for col in range(cols):
                for k in mat1_nonzero.keys():
                    res[row][col] += mat1_nonzero[k] * mat2[k][col] 

        return res