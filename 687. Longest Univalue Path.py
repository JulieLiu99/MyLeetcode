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
        At the end of each recursion, return the longest length using that node as the root.
        Set left/right to 0 whenever current node != parent node value.
        
        Time: O(n)
        Space: O(n)
        
        """
        self.longest = 0
        
        def traverse(node, parent_val):
            if not node:
                return 0
            
            left = traverse(node.left, node.val), 
            right = traverse(node.right, node.val)
            self.longest = max(self.longest, left+right)
            
            if node.val == parent_val:
                return 1 + max(left, right)
            else:
                return 0
        
        traverse(root, None)
        return self.longest
