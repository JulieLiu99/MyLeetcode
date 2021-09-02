# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        """
        Check all cells, col by col, until there is a 1 in one col
        -> Too many calls of BinaryMatrix.get
        Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.
        
        Time O(row * col)
        Space O(1)
        
        """
#         rows, cols = binaryMatrix.dimensions()
#         res = cols

#         for col in range(cols):
#             for row in range(rows):
#                 if binaryMatrix.get(row,col) == 1:
#                     return col
                
#         return -1

        """
        Take advantage of "row-sorted " feature
        
        Check row by row instead of col by col first
        Find the first col index in first row, where there is 1
        Then for future rows, only look for smaller col where there is 1
        
        Time O(row + col): only going lower left direction
        Space O(1)
        
        """
                
        rows, cols = binaryMatrix.dimensions()
        res = cols
        
        col = cols - 1
        for row in range(rows):
            while col >= 0 and binaryMatrix.get(row, col) == 1:
                res = min(res, col)
                col -= 1
            
        return res if res != cols else -1
