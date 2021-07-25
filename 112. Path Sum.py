# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        
        """
        Recursion until reach the leaf
        
        Time O(n)
        Space O(n)
        
        """
        
        if not root: return False
        
        if not root.left and not root.right: # leaf
            return root.val == targetSum
        
        if root.left and root.right:
            return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)
        
        elif root.left:
            return self.hasPathSum(root.left, targetSum-root.val)
        
        elif root.right:
            return self.hasPathSum(root.right, targetSum-root.val)
        
