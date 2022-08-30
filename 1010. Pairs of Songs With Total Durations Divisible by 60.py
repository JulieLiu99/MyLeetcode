class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        # Two Sum with K = 60
        
        # For each t, find x such that 
        # (t + x) % 60 = 0   =>   x % 60 + t % 60 = 0
        
        # Time O(n)
        # Space O(n)
        
        count = collections.defaultdict(lambda: 0)
        res = 0
        for t in time:
            x = - t % 60
            res += count[x]
            count[t % 60] += 1
        return res
