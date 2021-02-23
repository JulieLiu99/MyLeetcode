class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        """
        DP, Check if sum of some elements can be half of total sum
        Time O(total_sum / 2 * n):  for each num, loop through extra list
        Space O(total_sum / 2): extra list = half of input length + 1
        
        e.g. [1, 2, 3]
        [T (0), F (1), F (2), F (3)]
        
        """
        total_sum = sum(nums)
        if total_sum & 1:   # if total_sum % 2 == 1 is odd
            return False    

        target = total_sum >> 1     # target = sum//2
        
        dp = [True] + [False]*target    # dp[0] = True
        
        for num in nums:
            
            for i in range(target, num - 1, -1):    # from right to left: target to num
                
                dp[i] = dp[i] | dp[i - num]     # True if there is complement 
                
        return dp[target] == True  # check if target is True
