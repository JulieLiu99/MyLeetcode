class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Two pointers, try all interval sums
        
        Sliding window is inclusive: [l: r+1]
        Use prefix sum instead of adding all values within window
        Sum for nums[l: r+1] = presum[r+1] - presum[l]
        presum[i] = nums[0] + ... + nums[i-1]

        Time O(n^2): for every l pointer, needs to try r pointer from l to n-1
        
        """
#         presum = [0] # presum[1] = nums[0]
        
#         for i in range(len(nums)):
#             presum.append(presum[-1] + nums[i])

#         counter = 0
        
#         for l in range(len(nums)):
#             for r in range(l, len(nums)):
#                 if presum[r+1] - presum[l] == k:
#                     counter += 1
        
#         return counter

        """
        Running Sum
        
        For each running sum, find how many previous subarrays sums to (running sum - k)
        
        Time O(n)
        Space O(n)
        
        """    
        running_sum = 0
        hashmap = {0: 1} # when running_sum = k, counter += 1
        counter = 0
        
        for num in nums:
            
            running_sum += num
            extra = running_sum - k
            
            if extra in hashmap:
                counter += hashmap[extra]
                
            if running_sum in hashmap:
                hashmap[running_sum] += 1
            else:
                hashmap[running_sum] = 1
            
        return counter