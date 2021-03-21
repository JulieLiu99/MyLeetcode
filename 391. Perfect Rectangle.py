class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        
        """
        
        Key idea: a perfect rectangle must have 4 corner points
        Time O(n)
        Space O(n)
        
        """
        
        hs = set()
        area = 0
        
        for rec in rectangles:
            
            bottom_left = (rec[0], rec[1])
            top_left = (rec[0], rec[3])
            bottom_right = (rec[2], rec[1])
            top_right = (rec[2], rec[3])
            area += (rec[2] - rec[0]) * (rec[3] - rec[1])
            
            for point in [bottom_left, top_left, bottom_right, top_right]:
                if point not in hs:
                    hs.add(point)
                else:
                    hs.remove(point)
                    
        if len(hs) != 4:
            return False
        
        hs = sorted(hs)
        first = hs.pop(0)
        last = hs.pop()
        
        return area == (last[0] - first[0]) * (last[1] - first[1])
