class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        (Min) Heap
        
        Time O(n + k log n)
        Space O(n)
        
        """        
#         c = Counter(nums)
#         heap = []
#         for val, count in c.items():
#             heap.append((-count, val))
        
#         heapify(heap)   # creating a heap takes O(n): n is length of list passed in
        
#         res = []
#         for _ in range(k):
#             neg_count, val = heappop(heap)
#             res.append(val)
        
#         return res

        """
        Bucket Sort
        
        Time O(n)
        Space O(n)
        
        """
        if len(nums) == 1:
            return nums
        
        c = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)] # index = frequency, element = num val
        res = []
        for val, count in c.items():
            bucket[count].append(val)
        
        for i in range(len(nums), -1, -1): # append to res from val of more counts -> larger index
            for j in range(len(bucket[i])):
                res.append(bucket[i][j])
                if len(res) == k:
                    return res
