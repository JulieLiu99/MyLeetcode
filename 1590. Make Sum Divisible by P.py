class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        """
        Prefix + Hashmap
        
        Calculate the remainder = sum(nums) % p.
        One pass, record the prefix sum in a hashmap.

        Then the question becomes:
        Find the shortest array with sum % p = remainder.

        prefix_sum_to_index[remainder] records the last index that make
        (nums[0] + nums[1] + .. + nums[i]) % p = remainder

        Time O(N)
        Space O(N)
        
        """
        
        remainder = sum(nums) % p
        min_len = len(nums)
        prefix_sum = 0
        prefix_sum_to_index = {prefix_sum : -1}
        
        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            prefix_sum_to_index[prefix_sum] = i
            
            key = (prefix_sum - remainder) % p
            if key in prefix_sum_to_index:
                min_len = min(min_len, i - prefix_sum_to_index[key])
                
        return min_len if min_len < len(nums) else -1   
