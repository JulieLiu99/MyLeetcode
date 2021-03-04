class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        """
        Time O(nlogn + n^2): sort, one for loop + one while loop
        Space depends on sorting algorithm, otherwise O(1)
        """
        
        nums.sort()
        
        N, result = len(nums), []
        
        for i in range(N):
            
            # skipping duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # we want a+b = -c
            target = nums[i]*-1
            l,r = i+1, N-1
            
            while l<r:
                if nums[l]+nums[r] == target:
                    result.append([nums[i], nums[l], nums[r]])
                    l = l+1
                    r = r-1
                    while l<r and nums[l] == nums[l-1]:
                        l = l+1
                elif nums[l] + nums[r] < target:
                    l = l+1
                else:
                    r = r-1
        return result
