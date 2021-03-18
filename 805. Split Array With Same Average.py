class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        
        """
        Change the quesiton to a N-sum problem:
        To find if
        1 element with sum = 1 * avg or
        2 elements with sum = 2 * avg or
        k elements with sum = k * avg

        The size of smaller list will be less than N/2+1, so 0 < i < N/2+1
        Recursively find a subset of n elements from nums with sum = target
        
        Time O(N^2 * sum(A))
        Space O(N * sum(A))
        
        """
        
        @lru_cache(None) # helps in reducing the execution time of the function by using memoization technique.
        
        def find(target, k, i):
            if k == 0: 
                return target == 0
            if target < 0 or k + i > n: 
                return False
            return find(target - nums[i], k - 1, i + 1) or find(target, k, i + 1)
        
        n, s = len(nums), sum(nums)
        for k in range(1, n // 2 + 1):
            
            # s1/n1 = s2/n2
            # s1/n1 = (s-s1)/(n-n1)
            # (n-n1)s1/n1 = s-s1
            # n*s1/n1 - s1 = s - s1
            # n*s1 = s*n1
            # s1 = s*n1/n
            if s * k % n == 0:  
                if find(s * k / n, k, 0) == True:
                    return True
        
        return False
