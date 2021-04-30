# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        """
        Postorder Traversal
        Set the left/right to 0 whenever current node value != parent node value
        
        Time: O(n)
        Space: O(n)
        
        """
        self.longest = 0
        
        def traverse(node, parent_val):
            if not node:
                return 0
            
            left, right = traverse(node.left, node.val), traverse(node.right, node.val)
            self.longest = max(self.longest, left+right)
            
            if node.val == parent_val:
                return 1 + max(left, right)
            else:
                return 0
        
        traverse(root, None)
        return self.longest
