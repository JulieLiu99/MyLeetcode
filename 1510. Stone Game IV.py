class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        
        """
        #DP bottom up
        #
        #Time O(n * sqrt(n))
        #Space O(n)
        """
        
        
        dp = [False] * (n+1)
        for i in range(1, n+1):
            for k in range(1, int(i**0.5)+1):
                if dp[i - k*k] == 0:    # opponent loses
                    dp[i] = True
                    break
        return dp[-1]

        
        """
        Recursion
        
        Time O(n sqrt(n)): For each of n positions we check at most sqrt(n) different moves
        Space O(n)
        
        """
        """
    @lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        if n == 0:
            return False
        k = int(math.sqrt(n))
        while k >= 1:
            if not self.winnerSquareGame(n - k*k):
                return True
            k -= 1
        return False
        """
