class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        """
        Brute Force: O(n^3)
        
        After sorting, if (i, j, k) is a valid triple, then (i, j-1, k), ..., (i, i+1, k) are also valid triples. No need to count them one by one.
        
        left ... right k

        Time O(n^2)
        Space O(n)
        
        """
        nums.sort()
        count = 0
        for k in range(len(nums)): 
            left = 0
            right = k - 1
            while left < right:
                if nums[left] + nums[right] + nums[k] < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1
        return count
