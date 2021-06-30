class Solution:
    def climbStairs(self, n: int) -> int:
        
        """
        Recursion
        
        Time Limit Exceeded
        Time O(n)
        Space O(n)
        
        """
#         def climb(x):
#             if x == n:
#                 return 1
#             elif x > n:
#                 return 0
#             else:
#                 return climb(x+1) + climb(x+2)

#         return climb(0)

        """
        DP
        
        Time O(n)
        Space O(n)
        
        """
        
        res = [0]*(n+1)     # res[0], {res[1]...res[n]}
        res[0] = res[1] = 1
        
        for i in range(2, n+1):
            res[i] = res[i-1] + res[i-2]
            
        return res[-1]
