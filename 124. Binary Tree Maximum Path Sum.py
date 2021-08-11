# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Post order traversal
        
        If sum of subtree is negative -> discard it
        
        Very important: when return to one level up, we can only keep ONE side of subtree,
        If parent of root and root are included, root.left and root.right can't be both in the sequence/path.
        
        Time O(n)
        Space O(height)
        
        """
        
#         self.res = float('-inf')
        
#         def postorder(root):
#             if not root.left and not root.right: 
#                 self.res = max(self.res, root.val)
#                 return root.val
            
#             if root.left and root.right:
#                 left_sum = postorder(root.left)
#                 right_sum = postorder(root.right)
#                 tree_sum = max(0, left_sum, right_sum) + root.val
#                 subtree_sum = max(0, left_sum) + max(0, right_sum) + root.val
#                 self.res = max(self.res, left_sum, right_sum, tree_sum, subtree_sum)
                
#             elif root.right:
#                 right_sum = postorder(root.right)
#                 tree_sum = max(0, right_sum) + root.val
#                 self.res = max(self.res, right_sum, tree_sum)
                
#             elif root.left:
#                 left_sum = postorder(root.left)
#                 tree_sum = max(0, left_sum) + root.val
#                 self.res = max(self.res, left_sum, tree_sum)

#             return tree_sum
        
#         postorder(root)
#         return self.res

        """
        Shortened Version
        
        self.res = max(self.res, subtree_sum) replaces:
        self.res = max(self.res, left_sum, right_sum, tree_sum, subtree_sum)
        
        We don't need to incoporate left_sum, right_sum -> already considered in prev recursion.
        We don't need to incorporate tree_sum = max(0, left_sum, right_sum) + root.val 
        -> will be considered in the next recursion.
        
        """
        self.res = float('-inf')
        
        def postorder(root):
            
            if not root: return 0
            
            left_sum = postorder(root.left)
            right_sum = postorder(root.right)
            subtree_sum = max(0, left_sum) + max(0, right_sum) + root.val
            self.res = max(self.res, subtree_sum)
            
            return max(0, left_sum, right_sum) + root.val
        
        postorder(root)
        return self.res
