# class MyHashSet:
#     """
#     Use Python dictionary for HashSet
#     Count as "built-in hash table libraries"
    
#     Time O(n) for contains()
#     Space O(n)
    
#     """

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.hashset = {}

#     def add(self, key: int) -> None:
#         self.hashset[key] = True

#     def remove(self, key: int) -> None:
#         self.hashset[key] = False

#     def contains(self, key: int) -> bool:
#         """
#         Returns true if this set contains the specified element
#         """
#         if key not in self.hashset:
#             return False
#         else:
#             return self.hashset[key]
                
    
class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None
        
class MyHashSet:
    """
    Use Python dictionary for HashSet
    Count as "built-in hash table libraries"
    
    Time O(n) for contains()
    Space O(n)
    
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.SIZE = 1000
        self.hashset = [ListNode(-1) for _ in range(self.SIZE)]

    def add(self, key: int) -> None:
        head = self.hashset[key % self.SIZE]
        current = head.next
        while current:
            if current.key == key: return
            current = current.next
        # create new node right after head
        current = ListNode(key)
        current.next = head.next    # these two lines can't be reversed!!
        head.next = current         # otherwise current.next = current:(
        return
        
    def remove(self, key: int) -> None:
        prev = self.hashset[key % self.SIZE]
        while prev.next:
            current = prev.next
            if current.key == key: 
                prev.next = current.next
                return
            prev = prev.next
        return
    
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        head = self.hashset[key % self.SIZE]
        current = head.next
        while current:
            if current.key == key: return True
            current = current.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
