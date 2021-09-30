class MovingAverage:
    """
    Queue

    next():
    
    Time: O(1): Queue takes O(1) to append and pop.

    Space: O(n): n is the size of queue.The algorithm needs to maintain two integers: sum and numVal, and a queue. So it uses linear space.
    
    """

    def __init__(self, size: int):
        self.length = 0
        self.size = size
        self.sum = 0
        self.queue = deque()

    def next(self, val: int) -> float:
        if self.length < self.size:
            self.length +=1
            self.queue.append(val)
            self.sum += val
        else:
            self.sum -= self.queue.popleft()
            self.queue.append(val)
            self.sum += val
        return self.sum/self.length



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
