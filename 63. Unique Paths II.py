class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        DP in place
        
        obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        if stone, mark obstacleGrid[i][j] as 0
        first row and column always 1 if no obstacle in middle
        
        Time O(n)
        Space O(1)
        
        """
        
        # check 0,0
        if obstacleGrid[0][0] != 1:
            obstacleGrid[0][0] = 1
        else:
            return 0
            
        # check first column
        for row in range(1, len(obstacleGrid)):
            if obstacleGrid[row][0] == 1:
                           obstacleGrid[row][0] = 0
                           continue
            obstacleGrid[row][0] = obstacleGrid[row-1][0]
            
        # check first row
        for col in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][col] == 1:
                           obstacleGrid[0][col] = 0
                           continue
            obstacleGrid[0][col] = obstacleGrid[0][col-1]
        
        # check rest of grid
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                           obstacleGrid[i][j] = 0
                           continue
                obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                
        return obstacleGrid[-1][-1]
