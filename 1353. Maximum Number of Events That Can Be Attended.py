class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        """
        Brute Force
        
        TLE
        
        Time O(n * length of event)
        Space O(100001)
        
        """
        
#         seen = [0] * 100001    
        
#         for start, end in sorted(events, key=lambda e:e[1]):
#           for day in range(start, end + 1):
#             if seen[day]: continue
#             seen[day] = 1
#             break
            
#         return sum(seen)
        
        """
        Priority Queue (min heap in python)
        
        pq keeps the current open events.
        
        Each day, we add new events starting on day d to the queue pq.
        We also remove the events that are already closed.
        Then we greedily attend the event that ends the soonest.
        
        Time O(nlogn): For sorting. Each even goes into pq once and gets out once, so O(n).
        Space O(n): pq[]
        
        """

        events.sort(key = lambda e: e[0])
        pq = [] # store ending time of available events (that have started already)
        res = 0
        i = 0
        n = len(events)
        cur_day = 0 
        
        while i < n or pq:
            
            if not pq:  # no more open events that have started already -> get a new event
                cur_day = events[i][0]
                
            while i < n and  events[i][0] == cur_day: # push all events starting today
                heappush(pq, events[i][1])
                i += 1
                
            heappop(pq)  # attend the event that ends the soonest
            res += 1
            
            while pq and pq[0] <= cur_day: # ignore events that have ended
                heappop(pq)
            
            cur_day += 1
           
        return res
