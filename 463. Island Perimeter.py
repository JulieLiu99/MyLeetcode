class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        Go row by row
        
        For each 1, (if boundary or)
                    if grid[row][col-1] != 1, count += 1 as left side
                    if grid[row][col+1] != 1, count += 1 as right side
                    if grid[row-1][col] != 1, count += 1 as top side
                    if grid[row+1][col] != 1, count += 1 as bottom side
                    
        Time O(n)
        Space O(1)
        
        1 1 1
        1 0 1
        
        """
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    if i == 0 or grid[i-1][j] != 1: # first row or top isn't 1
                        count += 1
                    if i == rows-1 or grid[i+1][j] != 1: # last row or bottom isn't 1
                        count += 1
                    if j == 0 or grid[i][j-1] != 1: # first col or left isn't 1
                        count += 1
                    if j == cols-1 or grid[i][j+1] != 1: # last col or right isn't 1
                        count += 1
        return count
