"""
Idea:
-----
Pre-doubling all the odd numbers, and then only do division to make numbers smaller
eg. [5,2,3] => [10,2,6]

Since numbers onluy become smaller, we can start with the largest number
1. Subtract it with the smallest number to get current deviation
2. Divid it by 2 and put it back

[2,6,10]: 10 - 2 = 8
[2,5,6]: 6 - 2 = 4
[2,3,5]: 5 - 2 = 3

When the larget number becomes odd, we cannot divide anymore => stop

Implementation:
---------------
1. Priority Queue (Max Heap)
- Need to mantually track the min number in the set
- Can have duplicates in the queue

2. Tree Set
- O(1) to get max/min in the set
- Automatically remove duplicates

Time O(n*logm*logn) where m is the max value. each pop and add is O(logn). each element pop&add O(log m) times.
Space O(n)

"""

from sortedcontainers import SortedList

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        
        ls = SortedList([val<<1 if val&1 else val for val in nums])
        
        ans = ls[-1] - ls[0]
        
        while not ls[-1] & 1:
            ls.add(ls.pop()>>1)
            ans = min(ans, ls[-1] - ls[0]) 
            
        return ans
