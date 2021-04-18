"""
Two dict + Doubly linked list

"""

"""
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None

class DLinkedList:

    #Both append(node) and pop(node=None) are in O(1) complexity.

    def __init__(self):
        self.dummy = Node(None, None) # dummy node
        self.dummy.next = self.dummy.prev = self.dummy
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def append(self, node):
        node.next = self.dummy.next
        node.prev = self.dummy
        node.next.prev = node
        self.dummy.next = node
        self._size += 1
    
    def pop(self, node=None):
        if self._size == 0:
            return
        
        if not node:
            node = self.dummy.prev

        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1
        
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self._size = 0
        self._capacity = capacity
        
        self._node = dict() # key: Node
        self._freq = collections.defaultdict(DLinkedList)
        self._minfreq = 0
        
    def _update(self, node):

        #This is a helper function:
        #
        #    1. pop the node from the old DLinkedList (with freq `f`)
        #    2. append the node to new DLinkedList (with freq `f+1`)
        #    3. if old DlinkedList has size 0 and self._minfreq is `f`,
        #       update self._minfreq to `f+1`
        #
        #All of the opeartions take O(1) time.

        freq = node.freq
        
        self._freq[freq].pop(node)
        if self._minfreq == freq and not self._freq[freq]:
            self._minfreq += 1
        
        node.freq += 1
        freq = node.freq
        self._freq[freq].append(node)

    def get(self, key: int) -> int:
        if key not in self._node:
            return -1
        
        node = self._node[key]
        self._update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self._capacity == 0:
            return
        
        if key in self._node:
            node = self._node[key]
            self._update(node)
            node.val = value
        else:
            if self._size == self._capacity:
                node = self._freq[self._minfreq].pop()
                del self._node[node.key]
                self._size -= 1
                
            node = Node(key, value)
            self._node[key] = node
            self._freq[1].append(node)
            self._minfreq = 1
            self._size += 1

"""


"""

Two dict

"keyfreq": key -> frequency
"freqkeys": freq -> keys

Time O(1) 
Space O(N)
"""
        
class LFUCache:

    def __init__(self, capacity: int):
        self.keyfreq = {}
        self.freqkeys = defaultdict(dict) # for easier nested dict
        self.capacity = capacity
        self.minfreq = 1
        
    def get(self, key: int) -> int:
        if key not in self.keyfreq: return -1
        
        freq = self.keyfreq.pop(key)
        val = self.freqkeys[freq].pop(key)
        
        if not self.freqkeys[freq] and self.minfreq == freq:
            self.minfreq += 1
            
        self.freqkeys[freq+1][key] = val
        self.keyfreq[key] = freq + 1
        
        return val
        
    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0: return
        
        if key in self.keyfreq:
            self.get(key)
            self.freqkeys[self.keyfreq[key]][key] = value
            return
        
        if len(self.keyfreq) >= self.capacity:
            k = next(iter(self.freqkeys[self.minfreq])) # Python dict keeps insertion time order
            self.freqkeys[self.minfreq].pop(k)
            self.keyfreq.pop(k)
            
        self.keyfreq[key] = 1
        self.freqkeys[1][key] = value
        self.minfreq = 1
    
    
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
