class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Binary Search
        Time O(nlogn)
        
        """
        def need_days(weights, capacity):
            cur = 0
            days = 1
            for weight in weights:
                if cur + weight > capacity:
                    days += 1
                    cur = 0
                cur += weight
            return days
        
        l = max(weights) - 1
        r = sum(weights) + 1
        while l + 1 != r:
            m = (l + r) // 2
            if need_days(weights, m) <= days: # meets requirement, try to search for smaller
                r = m
            else: 
                l = m
        return r
