class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        """
        Brute Force:
        At every starting point, for every width (number of cols right), try all height (number of rows down)
        
        DP:
        The solution is based on largest rectangle in histogram solution. 
        Every row in the matrix is viewed as the ground with some buildings on it. 
        The building height is the count of consecutive 1s from that row to above rows. 

        Go row by row:
            1. update heights[col] for each col
            2. append [start, height] to stack
                    if there are previous higher ones:
                        pop previous higher ones and calculate their area
                        because their end point cannot extend anymore
                        extend start point of current height to left
                    append [start point, current height] to stack
            3. pop all [start, height] from right to left
                    their width is (width of matrix - their start point)
                    
        Time O(n): each height on each row is appended and poppped exactly once
        Space O(n)
                    
        """
        if not matrix or not matrix[0]:
            return 0
        
        width = len(matrix[0])
        heights = [0] * width
        maxArea = 0
        
        for row in range(len(matrix)):
            
            for col in range(width):
                if matrix[row][col] == '1':
                    heights[col] += 1
                else:
                    heights[col] = 0
                
            stack = []    # [start point, non decreasing height]
            for col in range(width):
                start = col
                height = heights[col]
                while stack and height < stack[-1][1]:
                    start, higher = stack.pop()
                    maxArea = max(maxArea, higher * (col - start))
                stack.append([start, height])
            
            while stack:
                start, height = stack.pop()
                maxArea = max(maxArea, height * (width - start))
                
        return maxArea
