class Solution:
    """
    1 10 10
    1  4  5
    2  3  6
    smallest = 1 + 1 + 2
    
    Merge two rows at a time by using the function kSmallestPairs.
    Loop through matrix row by row.
    Keep the smallest k sums from the chosen candidates from previous rows.
    
    To find the k smallest sums out of two rows, use Heap (min heap).
    Pop and keep the smallest sum from heap, if we don't have k smallest sums yet.
    Go one step right in one of the rows and push sum of elements to heap.
    Use a set to avoid duplicates.
    
    Heap: sum_ij, (i, j)
    “heapq” module in Python: the smallest of heap element is popped.                       Whenever elements are pushed or popped, heap structure in maintained.

    The time complexity of kSmallestPairs is k * logk. Since it is called m-1 times, we have total time complexity = k * logk * (m-1).

    Note: k * logk * (m-1) <= 200 * log(200) * 40.

    Time O(k * logk * (m-1))
    Space O(k)
    
    """
    
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        
        if not mat: return 0
        res = mat[0]
        
        for row in range(1, len(mat)):
            res = self.kSmallestSums(res, mat[row], k)
            
        return res[-1]
    
    
    def kSmallestSums(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        
        res = []
        visited = set()
        heap = [(nums1[0] + nums2[0], (0, 0))]
        
        while len(res) < k and heap:
            
            sum_, (i, j) = heapq.heappop(heap)
            res.append(sum_)
            
            if j+1 < len(nums2) and (i, j+1) not in visited:
                heapq.heappush(heap, (nums1[i] + nums2[j+1], (i, j+1)))
                visited.add((i, j+1))
                
            if i+1 < len(nums1) and (i+1, j) not in visited:
                heapq.heappush(heap, (nums1[i+1] + nums2[j], (i+1, j)))
                visited.add((i+1, j))       
                
        return res
