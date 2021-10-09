class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        DP
        
        DP[i]: the longest increasing subsequence up to nums[i]    
        
        Time O(n^2)
        Space O(n)
        
        """
        # dp = [1 for _ in range(len(nums))]
        # for i in range(1, len(nums)):
        #     for j in range(0, i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j]+1)
        # return max(dp)
        
        """
        Binary search
        
        Keep the current longest subsequence
        If next num is bigger than all, append at the end
        If next num is in middle, update that element (we want tail to be small)
        e.g. 12434
             1
             12
             124
             123
             1234
             
        Time O(nlogn)
        Space O(n)
        
        """
        sequence = []
        for num in nums:
            i = bisect.bisect_left(sequence, num)
            if i == len(sequence):
                sequence.append(num)
            else:
                sequence[i] = num
        return len(sequence)
