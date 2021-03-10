"""
Boundary Count 

https://www.youtube.com/watch?v=yK9a-rT3FBQ

Time O(N^2 logN): For each new event, traverse counter in O(N) time. Sorting takes extra O(logN) per event.

Space O(N): Size of counter.

"""

class MyCalendarThree(object):

    def __init__(self):
        # a dict subclass for counting hashable objects
        # count of a missing element is zero
        self.counter = collections.Counter() 

    def book(self, start, end):
        self.counter[start] += 1
        self.counter[end] -= 1

        active = ans = 0
        for x in sorted(self.counter):
            active += self.counter[x]
            if active > ans: 
                ans = active

        return ans
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
