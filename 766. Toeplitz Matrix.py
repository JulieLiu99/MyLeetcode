class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
        Going diagonally to bottom right from (0, 0): i+1, j+1
        Check for row indexes: 0 ~ rows-1, col = 0 as starting points
             then col indexes: 1 ~ cols-1, row = 0 as starting points
        
        Time O(n)
        Space O(1)
        
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range(rows):
            j = 0
            while i+1 < rows and j+1 < cols:
                if matrix[i+1][j+1] != matrix[i][j]:
                    return False
                i += 1
                j += 1
                
        for j in range(1, cols):
            i = 0
            while i+1 < rows and j+1 < cols:
                if matrix[i+1][j+1] != matrix[i][j]:
                    return False
                i += 1
                j += 1
                
        return True
