class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Binary search
        Min of k is 1, bc k is integer
        Max of k is max(piles), bc k > current pile, she only eats up the current pile
        
        Time O(log(max(piles)) * N)
        Space O(1)
        
        """
        l, r = 1, max(piles)
        while l < r:
            m = l + (r-l) // 2
            time = sum([math.ceil(i/m) for i in piles])
            if time > h:
                l = m + 1
            else:
                r = m
        return l


