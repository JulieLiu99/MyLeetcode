"""
Use hashmap 

Assuming vectors have number of nonzero values = n1 & n2
dotProduct: Time O(min(n1, n2))
Space O(n1 + n2)

If just one sparse vector:

Get the non-zero vals, and their indexes only from the sparse vector
Ignore other indexes when multiplying, because 0 * anything = 0
Only try to multiply those non-zero vals with corresponding vals in the second vector

"""

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeros = {idx:val for idx,val in enumerate(nums) if val != 0}

    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        
        if len(self.nonzeros) > len(vec.nonzeros):  # only loop through the smaller vector
            self.nonzeros, vec.nonzeros = vec.nonzeros, self.nonzeros
            
        for idx in self.nonzeros.keys():
            if idx in vec.nonzeros:
                res += self.nonzeros[idx] * vec.nonzeros[idx]
        return res

"""
Use lists and two pointers

dotProduct: Time O(min(n1, n2))
Space O(n1 + n2)

"""
class SparseVector:
    def __init__(self, nums: List[int]): 
        self.indexes = []
        self.vals = []
        for i, num in enumerate(nums):
            if num != 0:
                self.indexes.append(i)
                self.vals.append(num)
        self.n = len(self.indexes)
        
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        i = j = 0
        while i < self.n and j < vec.n:
            if self.indexes[i] == vec.indexes[j]:
                res += self.vals[i] * vec.vals[j]
                i += 1
                j += 1
            elif self.indexes[i] > vec.indexes[j]:
                j += 1
            else:
                i += 1
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
