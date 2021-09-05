class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        a building has an ocean view if all the buildings to its right have a smaller height.
        
        -> mono decreasing stack
        
        Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.
        
        Go through the heights from right to left
        Keep a maximum height (initialized as 0)
        If current height is larger than max, record index and update max
        Return the reversed recorded indexes
        
        Time O(n)
        Space O(1)
        
        """
        
        n = len(heights)
        res = []
        max_height = 0
        
        for i in range(n-1, -1, -1):
            if heights[i] > max_height:
                res.append(i)
                max_height = heights[i]
        
        return res[::-1]
