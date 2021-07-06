class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        """
        Prefix and Postfix products
        
        3 traversals of nums
        
        answer[i] = nums[0] ... nums[i-1] * nums[i+1] ... nums[n-1]
        pre[i] = nums[0] ... nums[i-1] (pre[1] = nums[0])
        post[i] = nums[i+1] ... nums[n-1] (pre[-2] = nums[n-1], pre[0] = nums[1]...nums[n-1])
         
        Time O(n)
        Space O(n)
        
        Correct but TLE :(
         
        """
#         n = len(nums)
#         answer = []
#         pre = [1]
#         post = [1]
        
#         for i, num in enumerate(nums):
#             pre.append(pre[i] * num)

#         for j in range(n-1, 0, -1): # till 0 instead of 1
#             post = [post[0] * nums[j]] + post

#         for k, num in enumerate(nums):
#             answer.append(pre[k] * post[k])
        
#         return answer
        
        """
        
        Reduce 3 traversal to 2
        
        Combine answer calcualtion and postfix products
        Go front to back once -> prefix products
        Go back to front once -> calculate answer and update postfix product
        
        Time O(n)
        Space O(n)
        
        Correct but still TLE :(
        
        """
#         n = len(nums)
#         answer = [0 for _ in range(n)]
#         pre = [1]
#         post = [1]
        
#         # pre[i] = nums[0] ... nums[i-1] (pre[1] = nums[0])
#         for i, num in enumerate(nums):
#             pre.append(pre[i] * num)
        
#         # post[i] = nums[i+1] ... nums[n-1] (pre[-2] = nums[n-1], pre[0] = nums[1]...nums[n-1])
#         for j in range(n-1, -1, -1): 
#             answer[j] = pre[j] * post[0]
#             post = [post[0] * nums[j]] + post
        
#         return answer
        
        """
        Record prefix and postfix products in-place in answer[]
        
        Go front to back once -> prefix products
        Go back to front once -> calculate answer and update postfix product
        
        Time O(n)
        Space O(1)
        
        """
        n = len(nums)
        product = 1
        answer = [1]
        
        # answer[i] = nums[0] ... nums[i-1] 
        # answer[1] = nums[0]
        # answer[n-1] = nums[0]...nums[n-2]
        for i in range(0, n-1):
            product *= nums[i]
            answer.append(product)
            
        product = 1
        for i in range(n-1, -1, -1):
            answer[i] *= product
            product *= nums[i]
            
        return answer
