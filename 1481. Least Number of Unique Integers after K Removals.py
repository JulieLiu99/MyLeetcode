class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        """
        Remove integers of least count
        
        Hashmap: val -> count
        Heap: sorted by count from small to large
        
        Time: O(n)
        Space: O(n)
        
        """
        counter = collections.Counter(arr)
        hp = [(count, val) for val, count in counter.items()]
        heapq.heapify(hp)
        
        while k > 0:
            k -= heapq.heappop(hp)[0]
            
        if k < 0:
            return len(hp) + 1
        else:
            return len(hp) 
