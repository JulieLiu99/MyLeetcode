class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Brute Force
        O(n^2)
        For each starting point, try all ending points
        
        Stack
        Record (start point, height) for each height
        Area = height * (end point - start point)
        
        If non-decreasing order 
            -> can extend end point till the end
            -> cannot extend start point
        If decreasing height 
            -> cannot extend end point anymore
            -> can extend start point to left
            
        Append into stack (current index as start point, height)
        Until its previous ones are higher
        Pop higher ones, calculate their termination area
        Extend current one's start point left
        
        At the end, use the length of array as end point and calculate areas
        
        Time O(n): each height gets append once and popped once
        Space O(n): stack
        
        """
        maxArea = 0
        stack = [] # (start point index, height)
        n = len(heights) 
        
        for i, height in enumerate(heights):
            # start point is its index
            # unless can extend to the left
            # when there are higher ones on the left
            start = i
            
            # pop existing heights that can no longer extend 
            # their end points, because newcommer is shorter
            while stack and stack[-1][1] > height:
                higher_start, higher = stack.pop()
                maxArea = max(maxArea, higher * (i - higher_start))
                start = higher_start
            
            stack.append((start, height))    # add new height
            
            for start, height in stack:
                maxArea = max(maxArea, height * (n - start))
                
            return maxArea
