class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        """
        1
        Brute Force recursion
        Find the minimum of largest sum among m subarrays of nums[i:]
        exceeded time limit despite @lru_cache(None)
        
        """
        """
        sums = [0]
        for x in nums: 
            sums.append(sums[-1] + x)
            
        @lru_cache(None)
        def fn(i, m): 
            
            if m == 1: return sums[-1] - sums[i]
            
            ans = inf #if not enough elements for m subarrays, inf is returned 
            if len(nums) < m: return ans
            
            for j in range(i+1, len(nums)): 
                ans = min(ans, 
                          max(fn(j, m-1), 
                              sums[j] - sums[i]))
            return ans
        
        return fn(0, m)
        """
        
        """
        2 
        DP
        still time limit exceeded
        Time O(mn^2)
        Space O(mn)
        
        """
        """
        dp = [[float("inf")]*(m+1) for _ in range(len(nums)+1)]
        acc = 0
        dp[0][1] = 0
        for i in range(1, len(nums)+1):
            acc += nums[i-1]
            dp[i][1] = acc

        for j in range(2, m+1):
            dp[0][j] = 0

        for j in range(2, m+1):     # m
            for i in range(j-1, len(nums)+1):       # length
                for i_ in range(i):     # splitting point
                    dp[i][j] = min(dp[i][j], max(dp[i_][j-1], dp[i][1]-dp[i_][1]))
                    
        return dp[len(nums)][m]
        """
        
        """
        3 
        Binary search
        Given a return result, compute the number of groups needed
        if number of groups > m, increase return result
           number of groups < m, decrease return result
           
        Time O(log(sum(nums)) * n)
        Space O(1)
        
        """
        l, r = max(nums), sum(nums) # the final result has to be between l and r
        while l < r:
            mid = (l + r) // 2
            count, cur_sum = 1, 0
            for n in nums:
                cur_sum += n
                if cur_sum > mid:
                    count += 1
                    cur_sum = n
            if count > m:
                l = mid + 1
            else:
                r = mid
                
        return l
