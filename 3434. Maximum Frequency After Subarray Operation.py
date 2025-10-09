class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        Sliding window

        Pick a target value in list to convert: target num's + x = k's

        For each target, find a contiguous segment where
        count(targets converted to k's) - count(k's lost in conversion) is largest

        Time O(n)
        Space O(n)
        """
        base = nums.count(k)
        best_gain = 0

        # try converting target num ≠ k into k
        for target in set(nums):
            if target == k:
                continue

            cur_gain = 0
            gain_with_target = 0 # best gain for this target overall

            for num in nums:
                if num == target: # this num would become k
                    cur_gain += 1 
                elif num == k: # this k would be "lost"
                    cur_gain -= 1
                if cur_gain < 0: # restart if window is net harmful 
                    cur_gain = 0
                gain_with_target = max(gain_with_target, cur_gain)

            best_gain = max(best_gain, gain_with_target)

        return base + best_gain
