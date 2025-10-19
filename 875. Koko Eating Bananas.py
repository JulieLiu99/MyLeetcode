class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Binary search
        Range of target is [1, max size of a single pile]
        
        Time O(log(max(piles)) * N)
        Space O(1)
        
        """
        l = 1
        r = max(piles)
        while l < r:
            m = l + (r-l) // 2
            time = sum([math.ceil(pile/m) for pile in piles])
            if time > h: # too slow
                l = m + 1
            else:
                r = m
        return l



