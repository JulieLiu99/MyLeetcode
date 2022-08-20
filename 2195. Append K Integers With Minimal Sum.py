class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        
        # Naive apporch: linear scan
        # Time O(n + k) : TLE
        # Space O(1)
        
        # count = 0 
        # min_sum = 0
        # i = 1
        # num_set = set(nums)
        # while count < k:
        #     if i not in num_set:
        #         min_sum += i
        #         count += 1
        #     i += 1
        # return min_sum
        
        
        # Assume the minimum sum we could get for k numbers:
        # [1, 2, ..., k] -> sum = k * (k+1) / 2
        # In case num within [1, 2, ..., k] already exists, replace it with (k+1) in sum
        
        # O(nlogn): good when k is large
        
        min_sum = k * (k+1) / 2
        
        nums.sort()
        
        for i, num in enumerate(nums):
            if i and nums[i] == nums[i-1]:
                continue
            if num <= k: 
                # extract from min_sum and add (k+1) instead
                min_sum = min_sum - num + (k+1)
                k += 1 # increment k+1
                
        return int(min_sum)
