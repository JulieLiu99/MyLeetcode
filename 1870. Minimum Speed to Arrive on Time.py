import math

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        """
        Binary Search
        
        Time: O(nlog(K)), where n = dist.length and K is the search space of speed
        Space: O(1)
        
        """
        
        l = 1
        r = 10 ** 7 + 1
        n = len(dist)
        
        if int(hour) < n-1: return -1
        
        while l < r:
            speed = l + (r - l) // 2
            need = sum(math.ceil(dist[i]/speed) for i in range(n - 1)) + dist[-1]/speed
            if need > hour:
                l = speed + 1
            else:
                r = speed
                
        if l == 10 ** 7 + 1:
            return -1
        else:
            return l  
        
