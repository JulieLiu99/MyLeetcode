class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
#         Solution 0: Recursion with memorization/ DP
        
#         dp(i) = max score we can get at position i
        
#         Base case: dp(0) = nums[0]
#         Transition: dp(i) = nums[i] + max(dp(j)), max(0, i-k) <= j < i
#         Answer: dp(n-1)
        
#         Time O((n-k) * k) => Time Limit Exceeded
#         Space O(n)
        
       
        """
        @lru_cache(None)
        def dp(i):
            if i == 0: return nums[0]
            return nums[i] + max(dp(j) for j in range(max(0, i-k), i))
        
        return dp(len(nums) - 1)
        """
        
#         Solution 1: DP + Monotonic Queue
        
#         Find max of a sliding window of size k:
#         max(dp(j)), max(0, i-k) <= j < i 
        
#         Monotonic Queue: 
#         Stores unique values of dp[i-k+1 ~ i] in descending order
        
#         Time O(n)
#         Space O(k)

#         nums = [10,-5,-2,4,0,3], k = 3
#         dp   = [10,5,8,14,14,17]
# 		  Deque at the beginning of each loop iteration:
#         i = 0    [(10,0)]        
#         i = 1    [(10,0), (5,1)]  
#         i = 2    [(10,0), (8,2)]  
#         i = 3    [(14,3)]       
#         i = 4    [(14,3), (14,4)]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        q = deque([(nums[0], 0)])
        
        for i in range(1, len(nums)):
            # nums[i] + max of sliding window
            dp[i] = nums[i] + q[0][0] 
            
            while q and q[-1][0] < dp[i]:   
                q.pop()      # pop smaller values at the back    
                
            q.append((dp[i],i))             
            
            if q[0][1] == i - k:              
                q.popleft()  # pop old value at the front   
                             # so in next round q[0][1] == (i+1) - k
                
        return dp[-1]
