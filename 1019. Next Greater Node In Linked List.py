# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        """
        Monotonic Stack
        
        Brute Force: one loop for each element O(n^2)
        
        Find the first greater element => Monotonic increasing stack
        [idx, val]
        
        Time O(N)
        Space O(N)
        
        """
        
        # convert the linked list into array, so that can traverse backward
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
            
        n = len(nums)
        stack = []  # idx of increasing vals
        ans = [0] * n
        
        for i in range(n-1, -1, -1):
            # ignore the nums smaller and older than current
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            
            # the first larger one is the answer
            if stack:
                ans[i] = stack[-1]
              
            # add current num as candidate for future smaller nums
            stack.append(nums[i])
            
            
        return ans
