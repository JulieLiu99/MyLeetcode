class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        """
        Priority Queue
        
        Sort tasks by enqueue time, keep original indexes.
        
        For each cur_time:
        Keep available tasks
            sorted by (processing time of available tasks - shortest to longest, index of task).
        Pick task by popping
        
        Time O(nlogn): Sorting takes O(nlogn). Processing tasks using Priority Queue takes O(n).
        Space O(n)
        
        """
        
        # Cannot just sort by starting time:
        # tasks.sort(key = lambda t:t[0])
        # We need to keep original indexes
        
        # (t[0], t[1], i) instead of [t[0], t[1], i] bc
        # Tuple is faster than List in Python 
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        pq = [] # to store (processing time of available tasks - shortest to longest, index of task)
        res = []
        
        i = 0
        n = len(tasks)
        cur_time = 0
        
        while i < n or pq:
            
            if not pq:  # no available tasks now, start from the next enqueue time
                cur_time = tasks[i][0]
                heappush(pq, (tasks[i][1], tasks[i][2]))
                i += 1
            
                while i < n and tasks[i][0] == cur_time:    # add all tasks available at this enqueue time
                    heappush(pq, (tasks[i][1], tasks[i][2]))  
                    i += 1 
                
            processing_time, idx = heappop(pq)   # process this one task 
            res.append(idx)
            cur_time += processing_time
            
            while i < n and tasks[i][0] <= cur_time:    # add all newly available tasks
                heappush(pq, (tasks[i][1], tasks[i][2]))  
                i += 1  
            
        return res
