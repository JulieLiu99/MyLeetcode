class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        Find how many non-overlapping intervals we have
        
        Time O(nlogn): sort
        Space O(n): sort
        
        """
        
        if len(points) == 0: return 0
        
        points.sort(key = lambda x: x[1])
        count = 1
        right = points[0][1]
        
        for point in points[1:]:
            
            if point[0] > right:    # no overlap --> one more shot
                count += 1
                right = point[1]
                
        return count 
