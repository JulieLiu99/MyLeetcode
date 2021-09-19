class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        Top right to bottem left: row+1, col-1
        Bottom left to top right: row-1, col+1
        
        Start from (0, 0) and got to top right
        Whenever hit row = 0/rows-1 or col = 0/cols-1, reverse direction
        
        Time O(n)
        Space O(1)
        
        """
        rows = len(mat)
        cols = len(mat[0])
        n = rows * cols 

        row = 0
        col = 0
        
        up = True
        result = []
        
        while len(result) < n:
            
            result.append(mat[row][col])
            
            if up: 
                
                if row > 0 and col < cols - 1: # go up right
                    row -= 1
                    col += 1
                    
                elif col == cols - 1: # at the right boundary, go down
                    row += 1
                    up = False   
                    
                else: # row == 0 # at the top boundary, go right
                    col += 1
                    up = False 
                    
            else:  
                 
                if row < rows - 1 and col > 0: # go bottom left
                    row += 1
                    col -= 1
                
                elif row == rows - 1: # at the bottom boundary, go right
                    col += 1
                    up = True 
                
                else: # col == 0 # at the left bounary, go down
                    row += 1
                    up = True 
            
        return result
