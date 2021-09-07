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
        
        res = 0
        
        for i in range(k):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
            res = nums[i]
        
        return res
