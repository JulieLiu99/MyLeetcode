class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        [running_sum % k = x][divisable subarray]
                                                ^ at this point ALSO running_sum % k = x
        Calculate the running sum and count it.
        
        Since key % k, therefore 0 <= key < k and we can use an array instead of hashmap
        
        """
        res = 0
        running_sum = 0
        count = [0] * k
        count[0] = 1
        for num in nums:
            running_sum = (running_sum + num) % k
            res += count[running_sum]
            count[running_sum] += 1
        return res
