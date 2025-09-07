"""
Two dict + Doubly linked list

key -> Node
freq -> DLinkedList (LRU order within same freq)

Time O(1)
Space O(N)
"""
# class Node:
#     def __init__(self, key, val):
#         self.key = key
#         self.val = val
#         self.freq = 1
#         self.prev = self.next = None

# class DLinkedList:

#     def __init__(self):
#         self.dummy = Node(None, None) # dummy node
#         self.dummy.next = self.dummy.prev = self.dummy
#         self._size = 0
    
#     def __len__(self):
#         return self._size
    
#     def append(self, node):
#         node.next = self.dummy.next
#         node.prev = self.dummy
#         node.next.prev = node
#         self.dummy.next = node
#         self._size += 1
    
#     def pop(self, node=None):
#         if self._size == 0:
#             return None
        
#         if not node:
#             node = self.dummy.prev

#         node.prev.next = node.next
#         node.next.prev = node.prev
#         self._size -= 1
        
#         return node

# class LFUCache:

#     def __init__(self, capacity: int):
#         self._size = 0
#         self._capacity = capacity
        
#         self._node = dict() # key: Node
#         self._freq = collections.defaultdict(DLinkedList)
#         self._minfreq = 0
        
#     def _update(self, node):

#         #This is a helper function:
#         #
#         #    1. pop the node from the old DLinkedList (with freq `f`)
#         #    2. append the node to new DLinkedList (with freq `f+1`)
#         #    3. if old DlinkedList has size 0 and self._minfreq is `f`,
#         #       update self._minfreq to `f+1`
#         #

#         freq = node.freq
        
#         self._freq[freq].pop(node)
#         if self._minfreq == freq and len(self._freq[freq]) == 0:
#             del self._freq[freq]
#             self._minfreq += 1
        
#         node.freq += 1
#         freq = node.freq
#         self._freq[freq].append(node)

#     def get(self, key: int) -> int:
#         if key not in self._node:
#             return -1
        
#         node = self._node[key]
#         self._update(node)
#         return node.val

#     def put(self, key: int, value: int) -> None:
#         if key in self._node:
#             node = self._node[key]
#             self._update(node)
#             node.val = value
#         else:
#             if self._size == self._capacity:
#                 node = self._freq[self._minfreq].pop()
#                 del self._node[node.key]
#                 self._size -= 1
                
#             node = Node(key, value)
#             self._node[key] = node
#             self._freq[1].append(node)
#             self._minfreq = 1
#             self._size += 1


"""
Two dict

"key2": key -> (value, freq)
"freq2": freq -> OrderedDict of keys (LRU within same freq)

Time O(1)
Space O(N)
"""
from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minfreq = 0
        self.key2 = {}                              # key -> (val, freq)
        self.freq2 = defaultdict(OrderedDict)       # freq -> OrderedDict(key -> None)

    def _bump(self, key: int):
        val, freq = self.key2[key]

        # remove from old bucket
        self.freq2[freq].pop(key)
        if not self.freq2[freq]:
            del self.freq2[freq]
            if self.minfreq == freq:
                self.minfreq = freq + 1
                
        # add to new bucket
        new_freq = freq + 1
        self.freq2[new_freq][key] = None
        self.key2[key] = (val, new_freq)
        return val, new_freq

    def get(self, key: int) -> int:
        if key not in self.key2:
            return -1
        val, _ = self._bump(key)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.key2:
            # update value and bump frequency
            _, new_freq = self.key2[key]
            self.key2[key] = (value, new_freq)
            self._bump(key)
            return

        # evict if full
        if len(self.key2) >= self.capacity:
            evict_key, _ = self.freq2[self.minfreq].popitem(last=False)
            del self.key2[evict_key]
            if not self.freq2[self.minfreq]:
                del self.freq2[self.minfreq]

        # insert new key at freq = 1
        self.key2[key] = (value, 1)
        self.freq2[1][key] = None
        self.minfreq = 1
    
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
