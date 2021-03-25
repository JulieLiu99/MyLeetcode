class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        """
        Time O(NlogN)
        Space O(1) for python sorting
        
        Sort input A first,
        For each A[i], find out the maximum A[j]
        that A[i] + A[j] <= target.

        For each elements in the subarray A[i+1] ~ A[j],
        we can pick or not pick,
        so there are 2 ^ (j - i) subsequences in total.
        So we can update res = (res + 2 ^ (j - i)) % mod.

        We don't care the original elements order,
        we only want to know the count of sub sequence.
        So we can sort the original A, and the result won't change.

        """
        
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        mod = 10**9 + 7
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += pow(2, r - l) % mod
                l += 1
        return res % mod
