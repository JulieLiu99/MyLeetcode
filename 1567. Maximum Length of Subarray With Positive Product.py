class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
        """
        DP
        
        "pos[i]", "neg[i]" represent longest consecutive numbers ending with nums[i] forming a positive/negative product.

        Time O(N)
        Space O(N)
        
        """
        
#         n = len(nums)
#         pos, neg = [0] * n, [0] * n
        
#         if nums[0] > 0: pos[0] = 1
#         elif nums[0] < 0: neg[0] = 1
            
#         ans = pos[0]
        
#         for i in range(1, n):
            
#             if nums[i] > 0:
#                 pos[i] = 1 + pos[i - 1]
#                 if neg[i - 1] > 0:
#                     neg[i] = 1 + neg[i - 1]  
                    
#             elif nums[i] < 0:
#                 neg[i] = 1 + pos[i - 1]
#                 if neg[i - 1] > 0:
#                     pos[i] = 1 + neg[i - 1] 
                
#             ans = max(ans, pos[i])
            
#         return ans

        """
        
        Space Optimization

        Since only the previous one value of pos/neg is used, we can use 2 variables instead of 2 lists.
        
        Time O(N)
        Space O(1)

        """

        n = len(nums)
        pos, neg = 0, 0
        
        if nums[0] > 0: pos = 1
        elif nums[0] < 0: neg = 1
            
        ans = pos
        
        for i in range(1, n):
            pos2 = neg2 = 0
            
            if nums[i] > 0:
                pos2 = 1 + pos
                if neg > 0:
                    neg2 = 1 + neg
                    
            elif nums[i] < 0:
                neg2 = 1 + pos
                if neg > 0:
                    pos2 = 1 + neg
                
            ans = max(ans, pos2)
            
            pos = pos2
            neg = neg2
            
        return ans
