class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        
        # Greedy: The earlier combined sticks are added more times, so if we want to minimize cost, we will want to combine the smaller ones as early as possible.
        
        # Time: heapify O(n), heappop & push O(nlogn)
        # Space: O(n)
        
        heapq.heapify(sticks)
        res = 0
        
        while len(sticks) > 1:
            x, y = heapq.heappop(sticks), heapq.heappop(sticks)
            res += x + y
            heapq.heappush(sticks, x + y)
            
        return res
