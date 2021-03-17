class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        """
        [kinda understand]
        
        Dynamic Programming

        https://www.youtube.com/watch?v=0RGxWCE2vzM

        Same problem as:
        Divide all numbers into two groups,
        what is the minimum difference between the sum of two groups.
        Now it's a easy classic knapsack problem.

        We want min(s2 - s1), s2 + s1 = sum
        --> return is min(s2 - s1) = (sum - s1) - s1 = sum - 2*s1
        
        Use dp to record the achievable sum of the smaller group s1
        dp[x] = 1 means the sum x is possible.        

        """

        target = int(sum(stones)/2)
        dp = [0] * (target+1)
        
        for i in stones:
            for j in range(target, i-1, -1):
                    dp[j] = max(dp[j], dp[j-i] + i)  # max(not include, include)
        
        return sum(stones) - 2 * dp[-1]
