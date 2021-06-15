class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        
        """
        Prefix Sum
        
        This problem is very similar to the max rectangular in histogram. 84 
        https://leetcode.com/problems/largest-rectangle-in-histogram/
        Just replace the "width" with the subarray sum, which can be obtained by prefix sum in O(1) time.
        
        https://www.youtube.com/watch?v=YLesLbNkyjA
        Keep mono increasing stack: (start_idx, val)
        Each val is the min of subarray from start_idx till end
        
        Initialize presum[i] = nums[0] + ... + nums[i-1].
        
        First loop, build the mono increasing stack. 
        If any larger numbers in the middle, calculate their val* (presum[i] - presum[start]).
        
        Second loop, calculate all the val * (presum[n] - presum[start]).
        
        Time O(n)
        Space O(n)
        
        """
        
        res = 0
        n = len(nums)
        mono_stack = [] # (start_idx, val) of mono increasing vals
        
        presum = [0]    # presum[i] = nums[0] + ... + nums[i-1]
        for num in nums:
            presum.append(presum[-1] + num)
            
        for i, num in enumerate(nums):
            newStart = i
            while mono_stack and mono_stack[-1][1] > num:
                start, val = mono_stack.pop()       # remove the bigger val
                curSum = presum[i] - presum[start]  # nums[start] + ... + before num
                res = max(res, val*curSum)
                newStart = start    # num is smallest since start
            mono_stack.append((newStart, num))
            
        for start, val in mono_stack:
            curSum = presum[n] - presum[start]  # sum from start till end
            res = max(res, val*curSum)
            
        return res % (10**9+7)
