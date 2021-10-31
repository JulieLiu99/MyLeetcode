# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def deepestDepth(node, depth): # post order
            if not node:
                return node, depth 
			
            left_child, left_depth = deepestDepth(node.left, depth + 1)
            right_child, right_depth = deepestDepth(node.right, depth + 1)    

            if left_depth > right_depth:
                return left_child, left_depth
            
            elif right_depth > left_depth:
                return right_child, right_depth
            
            else: # both sides have deepest nodes, return root of subtree
                return node, left_depth
            
        return deepestDepth(root, 0)[0]
