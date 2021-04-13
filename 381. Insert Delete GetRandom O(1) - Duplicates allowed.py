class RandomizedCollection:
    
    """
    When removing an element, find the index of the last item in its dictionary entry     (which is a list).
    Swap it with the actual last element in the numbers list you are maintaining.         (Some corner cases need to be handled here).
    
    Time O(1)
    Space O(n)
    
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals, self.idxs = [], collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.vals.append(val)
        self.idxs[val].add(len(self.vals) - 1)
        return len(self.idxs[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if self.idxs[val]:
            idx = self.idxs[val].pop()
            last = self.vals[-1]
            self.vals[idx] = last
            self.idxs[last].add(idx)
            self.idxs[last].discard(len(self.vals) - 1)
            self.vals.pop()
            return True
        return False 

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.vals)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
