# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        """
        Recursion
        Time O(N): N is number of nodes. Worst case would visit all nodes.
        Space O(H): Worst case recursion stack takes N, which is the highest possible height of unbalanced BST.

        
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        else: # current root value is between the values of p and q --> Common Ancestor 
            return root
        """
        
        """
        Iteration
        Time O(N): N is number of nodes. Worst case would visit all nodes.
        Space O(1): No additional space.
        """
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root
