# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        DFS
        Find the root first, then recursively build each left and right subtree.
        
        Time O(n logn): it takes O(n) to slice the array each time. could pass indexes to optimize.
        Space O(n): passing the entire nums array.
        
        """
        
#         if not nums:
#             return None

#         mid = len(nums) // 2

#         root = TreeNode(nums[mid])
#         root.left = self.sortedArrayToBST(nums[:mid])
#         root.right = self.sortedArrayToBST(nums[mid+1:])

#         return root

        """
        Optimized version
        
        Time O(n): have to go through all n elements once
        Space O(logn): the maximum length of the stack is log n.
        
        """
        def dfs(nums, l, r):
            if l + 1 ==  r:
                return None

            m = (l + r) // 2
            node = TreeNode(nums[m])
            node.left = dfs(nums, l, m)
            node.right = dfs(nums, m, r)

            return node

        return dfs(nums, -1, len(nums))
