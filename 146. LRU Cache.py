"""

Python Dict + Double LinkedList
- access to a random key in O(1) --> hashtable
  key: pointer to node in list
- remove the last entry in LRU cache in O(1) --> list
  tail is the least recently used
- add/move an entry to the front of LRU cache in O(1) --> list

get and put in O(1) time 

"""

class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self._remove(self.dic[key])
        node = Node(key, value)
        self._add(node)
        self.dic[key] = node
        if len(self.dic) > self.capacity:
            node = self.tail.prev
            self._remove(node)
            del self.dic[node.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        n.prev = p
        p.next = n

    def _add(self, node):
        n = self.head.next
        n.prev = node
        self.head.next = node
        node.prev = self.head
        node.next = n
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
