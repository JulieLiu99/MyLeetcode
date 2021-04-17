"""
Doubly-linked list + Dictionary

Choosing data structure:
    query by key: Hash table
    get min/max: List
    incre/decre: List

Hash table: key --> pointer to list node
List node: value + {keys}, ordered

Time O(1)
Space O(n)

"""
    
class Node(object):

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.keys = set()
        
class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(0)
        self.tail = Node(0, self.head)
        self.head.next = self.tail
        self.mapping = defaultdict(lambda: self.head) # Define the dict and pass lambda
                                                      # as default_factory argument

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        cur = self.mapping[key]
        cur.keys.discard(key)
            
        if cur.val + 1 == cur.next.val:
            new = cur.next
        else:
            new = Node(cur.val + 1, cur, cur.next)
            new.prev.next = new.next.prev = new
            
        new.keys.add(key)
        self.mapping[key] = new

        if not cur.keys and cur.val != 0:
            cur.prev.next, cur.next.prev = cur.next, cur.prev

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if not key in self.mapping: return

        cur = self.mapping[key]
        cur.keys.discard(key)
        self.mapping.pop(key)

        if cur.val > 1:
            if cur.val - 1 == cur.prev.val:
                new = cur.prev
            else:
                new = Node(cur.val - 1, cur.prev, cur)
                new.prev.next = new.next.prev = new
                
            new.keys.add(key)
            self.mapping[key] = new

        if not cur.keys:
            cur.prev.next, cur.next.prev = cur.next, cur.prev

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        if not self.tail.prev.val: return ''
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if not self.head.next.val: return ''
        return next(iter(self.head.next.keys))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()