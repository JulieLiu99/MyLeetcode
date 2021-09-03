class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        answer[i] = product of all the elements of nums except nums[i]
        
        prefix product
        prefix[i] = nums[0] * ... * nums[i-1]
        
        res[i] = prefix[i] * prefix[n] // prefix[i+1]
        !!!! MIGHT BE // 0
        
        suffix product also
        suffix[i+1] = nums[i+1] * ... * nums[n-1]
        
        res[i] = prefix[i] * suffix[i+1]
        
        Time O(n)
        Space O(n)
        
        """
#         n = len(nums)
        
#         prefix = [1] # prefix[1] = nums[0]
#         for i in range(n):
#             prefix.append(prefix[-1] * nums[i])
            
#         suffix = [1] # suffix[1] = nums[n-1]
#         for i in range(n-1, -1, -1):
#             suffix.append(suffix[-1] * nums[i])
        
#         """
#         suffix[:] = suffix[::-1] # suffix[n-1] = nums[n-1]
        
#         res = []
#         for i in range(n):
#             res.append(prefix[i] * suffix[i+1])
#         """
#         # without reverse
        
#         res = []
#         for i in range(n):
#             res.append(prefix[i] * suffix[n-i-1])
            
#        return res
    
        """
        Running Product
        
        Time O(n): two loops through nums, combine suffix with getting res
        Space O(1): instead of arrays, use running product variables 
        
        """
        
        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)): # get prefix products
            res[i] = prefix * nums[i]
            prefix *= nums[i]

        suffix = 1 # get suffix products, then prefix product * suffix product 
        for i in range(len(nums)-1, -1,-1):
            if i == 0:
                res[i] = suffix
                break
            res[i] = res[i-1] * suffix # prefix product * suffix product
            suffix = suffix * nums[i]
            
        return res