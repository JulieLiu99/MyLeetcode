# class MyHashMap:
    
"""
Use Python dictionary
might count as "built-in hash table libraries"

"""

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.hashmap = {}

#     def put(self, key: int, value: int) -> None:
#         """
#         value will always be non-negative.
#         """
#         self.hashmap[key] = value

#     def get(self, key: int) -> int:
#         """
#         Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
#         """
#         if key in self.hashmap and self.hashmap[key] != -1:
#             return self.hashmap[key]
#         else:
#             return -1

#     def remove(self, key: int) -> None:
#         """
#         Removes the mapping of the specified value key if this map contains a mapping for the key
#         """
#         self.hashmap[key] = -1

        
"""
Naive implementation of Hash with chaining. 
Array of Linked Lists
[] -> [] -> []
[]
[] -> []
.
.
.
[] -> [] -> [] -> []

One can play with SIZE (number of slots in HashTable) to optimize the runtime. Currently SIZE = 1000.

Time O(n): when adding and removing, O(1) instead of O(n) for just a list of size 10^6
Space O(n): more efficient thatn a list of size 10^6

"""
        
class ListNode:
    def __init__(self, key):
        self.key = key
        self.val = None
        self.next = None

class MyHashMap:

    def __init__(self):
        # initialize a list of 1000 nodes
        self.SIZE = 1000
        self.hashing = [ListNode(-1) for _ in range(self.SIZE)]

    def put(self, key: int, value: int) -> None:
        head = self.hashing[key % self.SIZE]
        current = head.next
        while current:  # taken
            # key already exists, update val
            if current.key == key: 
                current.val = value
                return
            current = current.next
        # create new node after head
        current = ListNode(key)
        current.next = head.next
        head.next = current
        current.val = value
        return

    def get(self, key: int) -> int:
        current = self.hashing[key % self.SIZE].next
        while current:
            if current.key == key: 
                return current.val
            current = current.next
        return -1   # can't find

    def remove(self, key: int) -> None:
        prev = self.hashing[key % self.SIZE]
        while prev.next:
            current = prev.next
            if current.key == key: 
                prev.next = current.next
                return
            prev = prev.next
        return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
