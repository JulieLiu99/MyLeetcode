class Solution:
    def specialArray(self, nums: List[int]) -> int:
        """
        Solution 1: Brute Force
        
        For every num, loop and count
        
        Time O(n^2)
        Space O(1)
        
        """
        
        # for i in range(1001):
        #     count=0
        #     for j in nums:
        #         if j >= i:
        #             count+=1
        #     if count == i:
        #         return i
        # return -1
        
        
        """
        Solution 2: Sort + Binary Search
        
        Sort in descending order
        Index means the count of [nums (other than self) >= self value]
        e.g. if i = 2, 2 numbers larger than or equal to 3 :)
        [0,4,3,0,4] --> [4,4,3,0,0]
                         0 1 2 3 4
                         
        If we find i == nums[i], there will be i + 1 items larger or equal to i, which makes array not special.
        e.g. if i = 3, 4 numbers larger than or equal to 3 :(
        [0,4,3,3,0,4] --> [4,4,3,3,0,0]
                           0 1 2 3 4 5
        Time O(sort) ~O(nlogn)
        Space O(sort) ~O(1)
        
        """
        nums.sort(reverse=True)
        left = 0
        right = len(nums)
        
        while left < right:
            mid = left + (right - left) // 2
            if mid < nums[mid]:
                left = mid + 1
            else:
                right = mid  
             
        if left < len(nums) and left == nums[left]:
            return -1 
        else:
            return left
