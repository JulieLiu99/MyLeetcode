"""
Use both a deque and a SortedList to keep track of the last m numbers, FIFO. 

Maintain the total sums. 

Examine the index at which the new number will be inserted into the SortedList and the index at which the oldest number will be removed from the SortedList. 

If the new number to be inserted will become one of the smallest/largest k numbers, add it to self.first_k/self.last_k and subtract out the current kth smallest/largest number. 

The operation for removing the oldest number is similar but the reverse. The only gotcha is the off-by-1 error.

Time O(logM) due to operations on the SortedList (essentially an order statistic tree). O(1) calculate is trivial.
Space O(M) due to the deque and SortedList.

"""

from sortedcontainers import SortedList

class MKAverage:

    def __init__(self, m: int, k: int):
        self.m, self.k = m, k
        self.deque = collections.deque()
        self.sortedNums = SortedList()
        self.total = self.first_k = self.last_k = 0

    def addElement(self, num: int) -> None:
        self.total += num
        self.deque.append(num)
        index = self.sortedNums.bisect_left(num)
        
        # x x x [ x x x | x x x | x x x ] x 
        #          ^
        # x x x [ x x x x | x x x | x x x ] x 
        # x x x [ x x x | x x x | x x x ] x x
        
        # insert into first k
        if index <= self.k - 1:  
            self.first_k += num
            if len(self.sortedNums) >= self.k:
                self.first_k -= self.sortedNums[self.k - 1]
        
        # x x x [ x x x | x x x | x x x ] x 
        #                           ^
        # x x x [ x x x | x x x | x x x x ] x 
        # x x x x [ x x x | x x x | x x x ] x
        
        # insert into last k, plus 1 here because bisect_left
        if index >= len(self.sortedNums) - self.k + 1:
            self.last_k += num
            if len(self.sortedNums) >= self.k:
                self.last_k -= self.sortedNums[-self.k]
                
        self.sortedNums.add(num)
        
        # remove extra num from the size m sliding window
        if len(self.deque) > self.m:
            num = self.deque.popleft()
            self.total -= num
            index = self.sortedNums.index(num)
            if index <= self.k - 1:
                self.first_k -= num
                self.first_k += self.sortedNums[self.k]
            elif index >= len(self.sortedNums) - self.k:
                self.last_k -= num
                self.last_k += self.sortedNums[-(self.k+1)]
            self.sortedNums.remove(num)

    def calculateMKAverage(self) -> int:
        if len(self.sortedNums) < self.m:
            return -1
        return (self.total - self.first_k - self.last_k) // (self.m - 2 * self.k)


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
