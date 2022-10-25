class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
     
        """
        Use a vertical line to scan from left to right. 
        
        Time O(nlogn): every node addition or removal takes O(logn) time
        Space O(n)
        
        """
        
        """
        # Leetcode doesn't have SortedList
        
        events = []
        for l, r, h in buildings:
            events.append((l, h, 1))
            events.append((r, h, 0))
            
        events.sort()
        
        ans = []
        active_heights = SortedList([0])
        n = len(events)
        i = 0
        while i < n:
            cur_x = events[i][0]
            
            # process all events with same x together
            while i < n and events[i][0] == cur_x:
                x, h, start = events[i]
                
                if start:   
                    active_heights.add(h)
                else:
                    active_heights.remove(h)
                    
                i += 1
            
            # check if the biggest height has changed
            if not ans or ans[-1][1] != active_heights[-1]:
                ans.append((cur_x, active_heights[-1]))
                
        return ans
        """
        
        """
        Max heap 
        
        We see the left most points first
        
        With multiple buildings at the same time, we only see the top one
        When top one ends, we see the next top one
        
        Time O(nlogn)
        Space O(n)
        """
        events = [(L, -H, R) for L, R, H in buildings] # start-building events
        events += [(R, 0, 0) for _, R, _ in buildings] # end-building events (0 is always after negative height)
        events.sort() # left -> right

        res = [[0, 0]] # [position, height]
        live = [(0, float("inf"))] # [-height, ending position]
        
        for pos, negH, R in events:
            
            # 1, pop buildings that are already ended
            while live[0][1] <= pos: 
                heappop(live)
                
            # 2, if it's the start-building event, make the building alive
            if negH: 
                heappush(live, (negH, R))
                
            # 3, if previous keypoint height != current highest height, add to skyline
            if res[-1][1] != -live[0][0]:
                res.append([pos, -live[0][0]])
                
        return res[1:]