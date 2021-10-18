class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Python built in sort
        
        Time O(nlogn)
        Space O(n)
        Very quick but ...
        
        """
        # nums.sort(reverse = True)
        # return nums[k-1]
        
        """
        Selection Sort: can sort regionally, doesn't need to first sort globally first
        
        -> Stop after we got kth elements sorted
        -> Instead of using an array for sorted elements, only keep track of the lastest element
           When loop ends, lastest is Kth 
        -> Largest instead of smallest, so sort in descending order
        
        Time O(kn)
        Space O(1)
        
        """
                
        # for i in range(k):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] < nums[j]:
        #             nums[i], nums[j] = nums[j], nums[i]        
        # return nums[k-1]
        
        """
        Quick Sort
        
        Time O(n)
        Space O(1)
        
        """
        if not nums: return
        pivot = random.choice(nums)
        left =  [x for x in nums if x > pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        
        L, M = len(left), len(mid)
        
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]