class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        """
        DP + Min-Max
        
        Time O(n^3): for each (i,M), go through 1 ~ 2*M+1
        Space O(n^2)
        
        """
        n = len(piles)
        cache = [[0]*(n+1) for i in range(n)]
        
        def solve(i, M):
            
            if i >= n: return 0
            
            M = min(M, n)
            
            if cache[i][M] > 0: return cache[i][M]
            
            if (i+2*M) >= n:
                cache[i][M] = sum(piles[i:n])
                return cache[i][M]
            
            best = -sys.maxsize - 1
            cur_sum = 0
            for l in range(1, 2*M+1):
                cur_sum += piles[i+l-1]
                best = max(best, cur_sum-solve(i+l, max(l,M)))
            cache[i][M] = best
            return cache[i][M]
        
        return (sum(piles[0:n]) + solve(0,1)) // 2