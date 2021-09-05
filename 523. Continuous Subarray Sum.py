class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        return true if nums has a continuous subarray of size at least two 
        whose elements sum up to a multiple of k (sum % k == 0)
        
        Brute Force: try all continuous subarrays O(n^2), and see if sum divids k without remainder
        
        -> Running Sum
        (b * k + remainder) - (a * k + remainder) = (b - a) * k
        Key is to find points where the running sum % k have the same remainder
        Store the in cache {remainder from rumming_sum % k: the first index where this occurs}
        
        {0 : -1}: -1 for 0 because e.g. [1 k-1 ...], can return k k when index of k-1 is 1.
        
        Time O(n)
        Space O(n)
        
        """
        
        cache = {0 : -1} # rumming_sum % k: the first index where this occurs
        running_sum = 0
        
        for i in range(len(nums)):
            running_sum += nums[i]
            remainder = running_sum % k 
            if remainder in cache:
                if i - cache[remainder] >= 2: # subarray of at least 2
                    return True
            else:
                cache[remainder] = i
            
        return False
