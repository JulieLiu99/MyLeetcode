class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Time O(N): visit all height values
        Space O(1): no additional storage
        
        """
        L = 0
        R = len(height) - 1
        
        width = len(height) - 1
        area = 0
        
        for w in range(width, 0, -1):
            
            area = max(area, min(height[L], height[R]) * w)
            
            # If height[L] < height[R], move L inside, else move R inside.
            
            if height[L] < height[R]:
                L += 1
            else:
                R -=1
                
        return area


