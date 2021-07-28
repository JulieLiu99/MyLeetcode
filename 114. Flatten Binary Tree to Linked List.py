# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        """
        Iteration
        
        Morris Traversal
        
        Level by level
        right_most_node_in_left_subtree.right = root.right
        root.right = root.left
        root.left = None
        -> move to next level: root = root.right
        
        Time O(n): need to visit every node
        Spac O(1): no additional space
        
        """
        
#         if not root: return 
        
#         while root:
            
#             if root.left: # if left subtree, move it to right
#                 left = root.left
#                 while left.right:
#                     left = left.right
#                 # left is the right most node in the left subtree
#                 left.right = root.right
#                 root.right = root.left
#                 root.left = None
                
#             root = root.right
            
#         return
        
        """
        Recursion
        
        Flatten both left subtree and right subtree, by calling self.flatten()
        Connect: None <- root -> left subtree -> right subtree
        
        Time O(n): need to visit every node
        Space O(height of tree): recursion stack
        
        """
        
        if not root: return 
        
        left = root.left
        right = root.right
        
        self.flatten(left)
        self.flatten(right)
        
        if left:
            while left.right: 
                left = left.right
            # left is the right most node in the left subtree
            left.right = right
            root.right = root.left
            root.left = None

        return 
