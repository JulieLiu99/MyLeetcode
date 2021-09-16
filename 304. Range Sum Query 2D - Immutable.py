class NumMatrix:
    """
    Prefix Sum in a Matrix
    
    self.matrx[i][j] = sum of upper left square till [i][j] (inclusive)
    
    When getting a region sum, just subtract/add upper & left & intersection from the bigger square
    
    Time O(n) for getting the prefix sums, O(1) for sumRegion
    Space O(n)
    
    """

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        
        # first column
        for i in range(1,rows):
            matrix[i][0] += matrix[i-1][0]
            
        # first row
        for i in range(1,cols):
            matrix[0][i] += matrix[0][i-1]
            
        # middle
        for i in range(1,rows):
            for j in range(1,cols):
                matrix[i][j] += matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]
                
        self.matrix=matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.matrix[row2][col2]
        
        # starting from row 0
        if row1 == 0:
            return self.matrix[row2][col2] - self.matrix[row2][col1-1]
        
        # starting from col 0
        if col1 == 0:
            return self.matrix[row2][col2] - self.matrix[row1-1][col2]
        
        # in the middle
        # entire block - upper side - left left + upper left intersection
        return self.matrix[row2][col2] - self.matrix[row1-1][col2] - self.matrix[row2][col1-1] + self.matrix[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
