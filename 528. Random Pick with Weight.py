class Solution:
    """
    Prefix Sum + Binary Search
    
    convert weights in to array of running sums 
    [1, 3]
    [1, 4]: [1, 2-3-4]
    For random value = 2/3/4, return 1
    
    Time O(n) for Solution(w)
    Time O(logn) for pickIndex
    Space O(n)
    
    """

    def __init__(self, w: List[int]):
        self.prefixSums = []
        total = 0
        for weight in w:
            total += weight
            self.prefixSums.append(total)

    def pickIndex(self) -> int:
        value = random.randrange(1, self.prefixSums[-1]+1)
        # return bisect.bisect_left(self.prefixSums, value)
        l = -1
        r = len(self.prefixSums) 
        while l + 1 != r:
            m = l + (r-l)//2
            if self.prefixSums[m] < value:
                l = m
            else:
                r = m
        return r

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
