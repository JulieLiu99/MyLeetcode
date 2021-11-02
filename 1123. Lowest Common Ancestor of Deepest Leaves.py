# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Time O(N) for one pass
        Space O(H) for recursion management

        """
        def post_order(root):
            if not root: 
                return None, 0
            
            left_lca, left_depth = post_order(root.left)
            right_lca, right_depth = post_order(root.right)
            
            if left_depth > right_depth: 
                return left_lca, left_depth + 1
            elif right_depth > left_depth: 
                return right_lca, right_depth + 1
            else: # both sides same depth
                return root, left_depth + 1
            
        return post_order(root)[0]
