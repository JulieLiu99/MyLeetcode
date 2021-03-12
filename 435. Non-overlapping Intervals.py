class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        """
        A classic greedy case: interval scheduling problem.
        
        1) always pick the interval with the earliest end time [implemented]
        2) or, always pick the interval with the latest start time
        
        --> the maximal capacity to hold rest intervals
        
        E.g. Suppose current earliest end time of the rest intervals is x. Then available time slot left for other intervals is [x:]. If we choose another interval with end time y, then available time slot would be [y:]. Since x ≤ y, there is no way [y:] can hold more intervals then [x:]. Thus, the heuristic holds.
                
        Time O(nlogn): sort overwhelms greedy search
        Space O(logn): sort
        
        """
        
        right = float('-inf')
        remove = 0
        
        for start, end in sorted(intervals, key=lambda x: x[1]):
            if start >= right: # no overlap
                right = end
            else:              # yes overlap
                remove += 1
                
        return remove
