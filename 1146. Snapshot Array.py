class SnapshotArray:
    """
    Instead of copying the whole array for each snapshot, only record the changes of set.

    Python set is implemented as a hash table: lookup/insert/delete in O(1) average.
    
    Time
    SnapshotArray(int length): O(N) 
    set(int index, int val): O(1)
    snap(): O(1)
    get(int index, int snap_id): O(N)
    
    Space O(number of set)
    """

    def __init__(self, length: int):
        self.snapshot = {i: {0: 0} for i in range(length)}
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.snapshot[index][self.snap_id] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        while snap_id > 0 and snap_id not in self.snapshot[index]:
            snap_id -= 1
        return self.snapshot[index][snap_id]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
