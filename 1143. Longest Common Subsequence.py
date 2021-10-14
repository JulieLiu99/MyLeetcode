class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if text1[row - 1] == text2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])

        return dp[m][n]
    
    
        # @functools.lru_cache(None)
        # def dfs(i,j):
        #     if i<0 or j<0:
        #         return 0
        #     if text1[i] == text2[j]:
        #         return dfs(i-1,j-1) + 1
        #     return max(dfs(i-1,j), dfs(i,j-1))
        # return dfs(len(text1)-1, len(text2)-1)
