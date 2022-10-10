class MedianFinder:
    """
    Two heaps
    Always make sure len(self.large) = len(self.small)
                  or
                     len(self.large) = len(self.small) + 1
    
    Time addNum O(logn)
    Time findMedian O(1)
    Space O(n)
    """

    def __init__(self):
        self.small = []  # the smaller half of the list, max heap, -max on top
        self.large = []  # the larger half of the list, min heap, min on top

    def addNum(self, num: int) -> None:
        
        # if same length, add to large
        if len(self.small) == len(self.large):
            max_from_small = -heappushpop(self.small, -num) # max([small], num)
            heappush(self.large, max_from_small)
            
        # if large has one more than small, add to small
        else:
            min_from_large = heappushpop(self.large, num) # min([large], num)
            heappush(self.small, -min_from_large)
                
    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2.0
        else:
            return self.large[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()