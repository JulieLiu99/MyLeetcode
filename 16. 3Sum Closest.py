class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        """
        Two pointers
        Time O(nlogn + n^2): sort, inner and outer loop
        Space depends on sorting algorithm, otherwise O(1)
        """
        
        # initiate minimum difference with a large value
        diff = float('inf')
        
        nums.sort()
        
        for i in range(len(nums)):
            
            l, r = i + 1, len(nums) - 1
            if diff == 0:
                break
            
            while (l < r):
                sum = nums[i] + nums[l] + nums[r]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    l += 1
                else:
                    r -= 1
                      
        # sum of three integers 
        return target - diff
