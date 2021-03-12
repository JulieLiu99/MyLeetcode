class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        """
        Sort on left first in ascending order.
        When left are same, we sort right in decending order.
        e.g. [[1, 4], [2, 8], [3, 6]]
        
        Time O(sort)
        Space O(sort)

        """
        
        intervals.sort(key=lambda a: (a[0], -a[1]))
        
        covered = 0
        right = intervals[0][1]
        
        for i, j in intervals[1:]:
            
            if j <= right:   # yes current is covered by right
                covered += 1
                
            right = max(right, j)
            
        return len(intervals) - covered
