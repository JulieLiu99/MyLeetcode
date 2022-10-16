class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        DP: bottom up
        either skip one or skip two
        Time O(n)
        Space O(1)
        
        """
        n = len(nums)
        dp = [0]* n # dp[i]: max robbed at nums[i]
        if n >= 1: dp[0] = nums[0]
        if n >= 2: dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            # robbed previous one, OR did not rob previous one -> rob this one
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1] 

        # # don't understand
        # rob1 = 0 # max robbed, if robbed 1 before -> can't rob this one
        # rob2 = 0 # max robbed, if did not rob 1 before -> rob this one!
        # for num in nums:
        #     temp = max(rob1 + num, rob2)
        #     rob1 = rob2
        #     rob2 = temp
        # return rob2