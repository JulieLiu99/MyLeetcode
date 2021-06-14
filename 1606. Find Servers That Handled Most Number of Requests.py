from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        
        """
        1. Check whether a server is available now
        - vector/array O(1)
        - Treeset O(logk)
        
        2. Find next available server
        - vector/array O(k)
        - Treeset O(logk)
        
        Use a treeset to track the available servers
        
        A min heap to track the servers that are handling requests
        
        Key: release time/ value: server id
        
        At arrival time t, release all servers that have release times <= t
        
        Time O(nlogk)
        Space O(k)
        
        """
        
        pq = []
        count = [0] * k
        available = SortedList()
        
        for i in range(k):
            available.add(i)
             
        for i, (arrival_time, request_load) in enumerate(zip(arrival, load)):
            while pq and arrival_time >= pq[0][0]:
                available.add(heapq.heappop(pq)[1])
                
            server = i % k
            idx = available.bisect_left(server)
            
            if idx == available.__len__():  # if did not find server
                if not available:
                    continue
                else:
                    idx = 0
                    
            selected = available[idx]
            available.remove(selected)
            count[selected] += 1
            heapq.heappush(pq, (arrival_time + request_load, selected))
            
        max_request = max(count)
        ans = []
        for i, c in enumerate(count):
            if c == max_request:
                ans.append(i)
        return ans
