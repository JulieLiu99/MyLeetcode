class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        """
        DP
        
        dp[i][j] = match all to way to word1[i-1] and word2[j-1]
        
        dp[i-1][j-1] + 1: replace word1[i-1] with word2[j-1]
        dp[i][j-1] + 1: add word2[j-1]
        dp[i-1][j] + 1: delete word1[i-1] 
        
        Time O(nm)
        Space O(nm)
        
        """
        
        n, m = len(word1), len(word2)
        # cannot don this!!
        # dp = [[0]*(m+1)] * (n+1)
        # ^ shallow copy only, one changes all change
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        # if other word is empty
        for col in range(1, m+1):
            dp[0][col] = col
        for row in range(1, n+1):
            dp[row][0] = row
        """
        dp: 
        [[0, 1, 2, 3], 
         [1, 0, 0, 0], 
         [2, 0, 0, 0], 
         [3, 0, 0, 0], 
         [4, 0, 0, 0], 
         [5, 0, 0, 0]]
        """
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1] + 1, dp[i-1][j] + 1)
                else: 
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                
        return dp[-1][-1]
