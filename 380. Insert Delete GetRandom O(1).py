class RandomizedSet:
    
    """
    Because time complexity has to be O(1)
    Use a random number generator to get a random index
    Store all numbers into an array -> use the random index to get a random number
    
    Use a hashmap for number lookup, used in insert() amd remove()
    In order to keep array and hashmap the same, esp. during remove(), store index of nums in array into hashmap, and use the index to remove num from array
    
    Time O(1)
    Space O(n)
    
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.hashmap = {} # val: idx in arr

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.hashmap:
            return False
        
        self.hashmap[val] = len(self.arr) # index of val in arr
        self.arr.append(val)
        return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.hashmap: 
            return False
        last_idx = len(self.arr) - 1
        last_element = self.arr[last_idx]
        if val != last_element: # swap val with last_element in arr
            idx = self.hashmap[val]
            self.arr[idx], self.arr[last_idx] = self.arr[last_idx], self.arr[idx]
            self.hashmap[last_element] = idx
        self.arr.pop()
        del self.hashmap[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.arr)
    
    
    """
    If getRandom can be O(n) 
    Then we only need a set to store nums
    When we call getRandom, convert set to array/tuple
    
    """
    
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.data = set()
        

#     def insert(self, val: int) -> bool:
#         """
#         Inserts a value to the set. Returns true if the set did not already contain the specified element.
#         """
#         if val not in self.data:
#             self.data.add(val)
#             return True
#         else:
#             return False
        

#     def remove(self, val: int) -> bool:
#         """
#         Removes a value from the set. Returns true if the set contained the specified element.
#         """
#         if val not in self.data:
#             return False
#         else:
#             self.data.remove(val)
#             return True
        

#     def getRandom(self) -> int:
#         return random.choice(tuple(self.data))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
