class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        DFS
        search for all paths from each element, get max path for each element
        Time O(2 ^ (m+n)): TLE
        """
        
#         m, n = len(matrix), len(matrix[0])
        
#         def dfs(i, j, prev):
            
#             if i < 0 or j < 0 or i >= m or j >= n or matrix[i][j] <= prev:
#                 return 0
            
#             # get longest incraesing path from next element
#             left = dfs(i, j-1, matrix[i][j])
#             right = dfs(i, j+1, matrix[i][j])
#             top = dfs(i-1, j, matrix[i][j])
#             bottom = dfs(i+1, j, matrix[i][j])

#             return max(left, right, top, bottom) + 1
        
#         res = -1
#         for i in range(m):
#             for j in range(n):
#                 res = max(res, dfs(i, j, -1))
#         return res

        """
        DFS + memorization: save partial result, reduce duplicate search
        
        dfs(x, y): max path length starting at (x, y)
        
        dfs(x, y) = 1 + max{dfs(neighbor with larger value)}
               or = 1        
               
        Time O(mn)
        Space O(mn)
        """
        m, n = len(matrix), len(matrix[0])
        
        dp = [[-1 for _ in range(n)] for _ in range(m)] # dp[i][j] = max path length from (i, j)
        
        def dfs(i, j, prev):
            if i < 0 or j < 0 or i >= m or j >= n or matrix[i][j] <= prev:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]
            
            left = dfs(i, j-1, matrix[i][j])
            right = dfs(i, j+1, matrix[i][j])
            top = dfs(i-1, j, matrix[i][j])
            bottom = dfs(i+1, j, matrix[i][j])
            
            dp[i][j] = max(left, right, top, bottom) + 1
            return dp[i][j]
        
        res = -1
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j, -1))
        return res
