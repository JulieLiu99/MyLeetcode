class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        """
        Result matrix: rows = rows1, cols = cols2
        
        Space O(cols1)
        Time O(rows1 * (cols1 + rows2 * cols2))
        
        """
        rows = len(mat1)
        cols = len(mat2[0])
        l = len(mat1[0])  # length of one multiplication
        res = [[0 for _ in range(cols)] for _ in range(rows)]
        for row in range(rows):
            vals = {}
            for col1 in range(l):
                if mat1[row][col1]:
                    vals[col1] = mat1[row][col1]
            if vals:
                for row2 in range(l):
                    for col in range(cols):
                        if mat2[row2][col] and row2 in vals:
                            res[row][col] += vals[row2] * mat2[row2][col] 
        return res
