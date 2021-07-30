class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        Priority Queue
        
        Sort queries and intervals.
        
        Iterate queries from small to big:

            If there are, remove all closed interval from the queue.
            Find out all open intervals [l, r].
            Add them to a priority queue (size, right).
            The head of the queue is the smallest interval size we want to record.
        
        Time O(nlogn + qlogq)
        Space O(n)
        
        """
        
        pq = [] # stores available intervals' (size, right), sorted from small to big
        
        intervals.sort(key = lambda interval:interval[0])  # sort intervals by left point
        
        queries = sorted((query, idx) for idx, query in enumerate(queries)) # sort queries left to right

        res = [-1 for _ in range(len(queries))]     # initialize result array, default is not found
        
        i = 0
        n = len(intervals)
        
        for (query, idx) in queries:
                
            while pq and pq[0][1] < query:  # remove intervals already ended
                heappop(pq)
            
            while i < n and intervals[i][0] <= query: # for all intervals started before query
                if intervals[i][1] >= query:          # add those that end after query
                    heappush(pq, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
                
            if pq:
                res[idx] = pq[0][0]   # record smallest size, among available intervals
                             
        return res
