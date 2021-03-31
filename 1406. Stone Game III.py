class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        """
        DP + MinMax
        
        Top-down recursion might exceed time limit
        Use bottom-up instead
        
        dp[i] means optimal score at stoneValue[i]
        
        Time complexity = problems * actions.
        Problems = start position. Actions = 1/2/3 stones.
        Time O(n)
        Space O(1)
        
        """
        n = len(stoneValue)
        dp = [-10**9] * n + [0,0,0]     # add additional 0s to keep index in range
        stoneValue += [0,0,0]
        
        for i in range(n-1, -1, -1):
            for k in (1, 2, 3):
                dp[i] = max(dp[i], sum(stoneValue[i:i+k]) - dp[i+k])

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
