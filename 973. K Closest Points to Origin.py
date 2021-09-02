class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        """
        Brute Force: 
        calculate distance to (0, 0), don't need square root for comparison purpose
        * import math -> math.sqrt(int)
        sort and return first k
        Time O(nlogn)
        Space O(n)
        
        """
        
        # points = sorted(points, key=lambda point : point[0]**2 + point[1]**2)
        # return points[:k]
    
    
        """
        Heap:
        binary heap, with O(log n) push and O(log n) pop
        
        Time O(nlogn)
        Space O(n)
        """
        
        heap = []
        for point in points:
            heapq.heappush(heap, (point[0]**2 + point[1]**2, point))
                           
        res = []
        for _ in range(k):
            point = heapq.heappop(heap)[1] 
            res.append(point)
          
        return res
