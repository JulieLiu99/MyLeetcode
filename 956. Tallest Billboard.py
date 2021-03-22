class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=iPRWkifQgoo
        
        dp[height_difference] = height_of_the_taller
        
        Time O(n*sum)
        Space O(n)
        """
        
        dp = dict()
        dp[0] = 0
        
        for h in rods:
            cur = collections.defaultdict(int)
            for s in dp:
                cur[s+h] = max(dp[s] + h, cur[s+h])
                cur[s] = max(dp[s], cur[s])
                cur[s-h] = max(dp[s], cur[s-h])
            dp = cur
            
        return dp[0]
