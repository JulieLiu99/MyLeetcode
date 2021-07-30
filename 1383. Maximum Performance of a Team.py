class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        """
        Priority Queue
        
        Add engineers to heap one by one:
            Heap keeps currently chosen engineers, and sorts them by speed low to high
            If enough engineers already, pop the slowest one
            Update maximum res with current set of engineers
        
        Time O(nlogn): O(nlogn) for sorting, and O(nlogk) for priority queue
        Space O(n)
        
        """
        
        
        engineers = sorted(zip(efficiency, speed), reverse=True) # efficiency high to low
        
        pq_speed = []
        sum_speed = 0
        res = 0
        
        for eff, spd in engineers:
            
            heappush(pq_speed, spd)
            
            if len(pq_speed) <= k:  # not enough engineers -> add this person
                sum_speed += spd
            else:                   # enough -> add this person and pop the least efficient
                sum_speed += spd - heappop(pq_speed)
                
            res = max(res, sum_speed * eff)
            
        return res % (10**9+7)
