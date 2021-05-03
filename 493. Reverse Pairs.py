
"""
Solution 1

Binary Indexed Tree

Search for all elements greater than twice of current element, 
While inserting the element itself into the BIT.

For all 2*j:
    Find count of i so that nums[i] > 2 * nums[j]

Time O(nlogn)
Space O(n)

"""
"""
class Solution(object):
    def reversePairs(self, nums):
        
        if not nums:
            return 0
        
        nnums = list(set(nums+[2*j for j in nums]))
        sorted_nums = sorted(nnums) # ascending order
        tree = BIT(len(sorted_nums))
        
        num_idx = {}
        for idx, num in enumerate(sorted_nums):
            num_idx[num] = idx+1
        
        count_of_i = 0
        for num in nums[::-1]:
            count_of_i += tree.addCount(num_idx[num] - 1) # i
            tree.update(num_idx[2*num], 1)                # 2*j
        
        return count_of_i
    
class BIT():
    def __init__(self, N):
        self.tree = [0]*(N+1)
        self.n = N+1
    
    def update(self, idx, val):
        while idx < self.n:
            self.tree[idx] += val
            idx += (idx & (-idx))
        return
    
    def addCount(self, idx):
        s = 0
        while idx > 0:
            s += self.tree[idx]
            idx -= (idx & (-idx))
        return s

"""
"""
Solution 2

Merge Sort

count = left reverse pair + right reverse pair
In each mergesort(), use 2 sliding pointers i (till mid), j (after mid) to count

split reverse pair

Time O(nlogn): each recursion O(n) to merge two sorted array, O(n) to count
Space O(n)

"""

class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def mergesort(l, r):
            if l >= r: 
                return 0
            
            mid = l + (r-l) // 2
            count = mergesort(l, mid) + mergesort(mid+1, r)
            
            nums[l:mid+1] = sorted(nums[l:mid+1]) # sort 1st half ascending
            nums[mid+1:r+1] = sorted(nums[mid+1:r+1]) # sort 2nd half ascending
            
            i = l
            j = mid + 1
            while (i <= mid and j <= r):
                if nums[i] > 2*nums[j]:
                    count += mid - i + 1 # all i's that form reverse pairs with j
                    j += 1
                else:
                    i += 1

            return count

        return mergesort(0, len(nums)-1)
