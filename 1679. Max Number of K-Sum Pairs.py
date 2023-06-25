class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
        Same as 2-sum
        Time: O(n)
        Space: O(n)
        """
        cache = defaultdict(int) # num: count of k-num
        num_ops = 0
        for i in nums:
            if cache[i] > 0: # found complement
                cache[i] -= 1
                num_ops += 1
            else:
                cache[k-i] += 1
        return num_ops
