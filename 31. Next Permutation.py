class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Search by pointers
        Thinking through heights
        Try not to touch front part -> so that we find only the next larger nums

                        [1, 3, 2, 8, 5, 4]
                               ^pivot   ^swap

                                  / \
                                 /    \
                                        \
                   
        after swap      [1, 3, 4, 8, 5, 2]
                                  ^peak

        after reverse   [1, 3, 4, 2, 5, 8]
        
        Time O(n)
        Space O(1)
        """
        
        # find the last "drop" searching from right
        # that's the num to bump for the next permutation
        pivot = None
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break
         
        # nums is descending -> already the largest arrangement
        if pivot is None:
            nums.reverse()
            return 
        
        # tail is mono decreasing
        # find the num that's just bigger than nums[pivot]
        swap = len(nums) - 1
        while nums[swap] <= nums[pivot]:
            swap -= 1
        nums[pivot], nums[swap] = nums[swap], nums[pivot]  
        
        # since nums is descending from peak onwards
        # reverse tail to get smallest nums among the greater arrangements
        peak = pivot + 1
        nums[peak:] = reversed(nums[peak:])
        return
        
        
        
