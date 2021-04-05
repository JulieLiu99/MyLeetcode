class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
        """
        DP: bottom up
        
        Time O(n^3)
        Space O(n^2)
        
        """

        n = len(arr)
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 0
            
        for d in range(1, n):
            for i in range(0, n-d):
                j = i + d
                for k in range(i, j):
                    rootVal = max(arr[i:k+1]) * max(arr[k+1:j+1])
                    dp[i][j] = min(dp[i][j], rootVal + dp[i][k] + dp[k+1][j])
                    
        return dp[0][n - 1]
        
        
        """
        DP: top down, recursion + memorization
        
        Time O(n^3)
        Space O(n^2)
        
        also works
        
        """
        """
        def dp(arr, l, r, cache):
            if (l, r) in cache:
                return cache[(l, r)]
            if l >= r:
                return 0

            res = float('inf')
            for k in range(l, r):
                rootVal = max(arr[l:k+1]) * max(arr[k+1:r+1])
                res = min(res, rootVal + dp(arr, l, k, cache) + dp(arr, k+1, r, cache))

            cache[(l, r)] = res
            return res
    
        return dp(arr, 0, len(arr)-1, {})
        """
        
