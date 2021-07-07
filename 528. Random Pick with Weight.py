"""
Get the probability range for each index idx_prob[]

Pick a random float [0, 1) in pickIndex()
Binary search through idx_prob[]

pickIndex():
Time O(logn)
Space O(n)

Pretty good performance already

Could reduce Space to O(1) by modifying w in place
    for i in range(1,self.n):
        w[i] += w[i-1]
        
"""

class Solution:

    def __init__(self, w: List[int]):
        self.idx_prob = []   # [probability range] for each index
        self.n = len(w)
        total = sum(w)
        start = 0
        for idx, prob in enumerate(w):
            self.idx_prob.append(start)
            start += prob/total
        
    def pickIndex(self) -> int:
        # pick a random float [0, 1)
        # binary search through idx_prob
        if self.n == 1: return 0
        rand = random.random()
        l = -1
        r = self.n
        while l+1 != r:
            mid = l + (r-l)//2
            if self.idx_prob[mid] <= rand and (mid==self.n-1 or (mid+1<self.n and rand < self.idx_prob[mid+1])):
                return mid
            elif self.idx_prob[mid] < rand:
                l = mid
            else:
                r = mid
        return l
    
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
