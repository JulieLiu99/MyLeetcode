"""
Prefix Tree

We can build a prefix tree (Trie) to answer
whether there is a number in the array that starts 
with a given substring in O(1)
- If there is only one path, follow that path
- if there are two paths, choose the complement one (1 - current_bit)

Move in the trie from highest bit to lowest bit
31 bits for signed 32-bit integers

For each number, query the trie in O(31)
Time O(31*n)
Space O(31*n)

Since all the queties are given at once (offline processing),
we can process them in any order.
1. Sort queries by limit
2. Sort numbers

We can build the trie on the fly:
Insert numbers that are less or equal to the limit of the current query, 
Query the trie to find the maximum xor of the current number 
and numbers in the given array that are <= limit.

Time O(sort)

"""

class Trie:
    def __init__(self):
        self.root = {}
        
    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            if cur not in node:
                node[cur] = {}
            node = node[cur]
                
    def query(self, num):
        if not self.root: 
            return -1
        node = self.root,
        xor = 0
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            if 1 - cur in node:
                node = node[1 - cur]
                xor |= (1 << i) # set ith bit xor result to 1
            else:
                node = node[cur]
        return xor

    
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        nums.sort()
        # sort queries by m, which is [1][1] within i, (x, m)
        # ~ sorted((m, x, i) for i, (x, m) in enumerate(queries))
        queries = sorted(enumerate(queries), key=lambda x: x[1][1])
        trie = Trie()
        ans = [-1] * len(queries)
        j = 0
        
        for i, (x, m) in queries:
            # build the trie on the fly
            while j < len(nums) and nums[j] <= m:
                trie.insert(nums[j])
                j += 1
            # query for the current x_i among nums<=m
            ans[i] = trie.query(x)
            
        return ans
