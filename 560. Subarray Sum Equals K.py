class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Brute force: Sliding window O(n^2) time
        
        Better: Prefix sum
        presum[i] = nums[0] + ... + nums[i]
        sum[i...j] = presum[j] - presum[i-1]
        
        Cannot sort + One pass: need continuous subarray
        
        Time O(n^2)
        Space O(n)
        
        TLE still :(
         
        """
#         res = 0
#         presum = [nums[0]]
#         n = len(nums)
        
#         # calculate prefix sum
#         for i in range(1, n):
#             presum.append(presum[i-1] + nums[i])
#             # i == 0, from first num onwards
#             if presum[i-1] == k: res += 1
#         if presum[n-1] == k: res += 1
        
#         # from second num onwards
#         for i in range(1, n):
#             for j in range(i, n):
#                 if presum[j] - presum[i-1] == k:
#                     res += 1
                    
#         return res
                
        """
        Running Sum
        
        Increment result when:
        sums[up to now] - sums[till a previous point] = k
        
        Time O(n)
        Space O(n)
        
        """
        res = 0
        sums = 0
        sum_count = collections.defaultdict(int)
        
        # If sums==k, it should've been sums-0=k. To account for this case, we include the 0.
        sum_count[0] = 1
        
        for num in nums:
            sums += num
            res += sum_count[sums-k]
            sum_count[sums] += 1
        
        return res
