class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        """
        Calculate the width and height of intersection area
        
        For two lines overlap is min(ends) - max(starts)
        -------
            -------
        """
        width = min(rec1[2], rec2[2]) - max(rec1[0], rec2[0])
        height = min(rec1[3], rec2[3]) - max(rec1[1], rec2[1])
        return width > 0 and height > 0
