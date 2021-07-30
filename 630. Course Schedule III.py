class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        """
        Priority Queue
        
        We start learning courses with earliest closing date first. 
        
        If we can't finish current course before its close date, 
        we can un-learn one of the previous course in order to fit current course in. 
        
        We can safely un-learn a previous course because it closes earlier and there is no way for it to be picked up again later. We pick up the one with longest learning time to un-learn, if the longest learning time happend to be the newly added course, then it is equivalent to not learning the newly added course.
        
        Time O(nlogn)
        Space O(n)
        
        """
        
        courses.sort(key=lambda c: c[1]) # sort by last day, early to late
        pq = []
        cur_day = 0
        
        for duration, lastday in courses:
            
            heappush(pq, -duration) # sorted by duration, longest to smallest
            cur_day += duration
            
            if cur_day > lastday:   # cannot meet lastday for this course
                cur_day += heappop(pq)
                
        return len(pq)
