class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        """
        Recursion + Memorization is costly   
        User dinamic programing instead

        2D DP
        dp[i][j] means the biggest number of stones you can get more than opponent, picking piles in piles[i] ~ piles[j].
        
        Time O(N^2)
        Space O(N^2)
        
        """
        """
        n = len(piles)
        dp = [[0] * n for i in range(n)]
        
        for i in range(n): dp[i][i] = piles[i]
            
        for l in range(1, n):
            for i in range(n - l):
                dp[i][i + l] = max(piles[i] - dp[i + 1][i + l], 
                                   piles[i + l] - dp[i][i + l - 1])
                
        return dp[0][-1] > 0
        """
    
        """
        1D DP
        dp[i] means the biggest number of stones you can get more than opponent, picking piles in piles[i] ~ piles[i+l].
        
        Time O(N^2)
        Space O(N)
        """   
        n = len(piles)
        dp = [0 for i in range(n)]
        for l in range(1, n):
            for i in range(n - l):
                dp[i] = max(piles[i] - dp[i + 1], piles[i + l] - dp[i])
        return dp[0] > 0
