class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Binary search
        Range of target is [1, max size of a single pile]
        
        Time O(log(max(piles)) * N)
        Space O(1)
        
        """
        l = 0
        r = max(piles) + 1
        while l + 1 != r:
            m = l + (r-l) // 2
            time = sum([math.ceil(pile/m) for pile in piles])
            if time > h: # too slow
                l = m
            else:
                r = m
        return r



