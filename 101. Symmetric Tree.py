# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        Recursion
        
        Time O(n)
        Space O(n)
        
        """
        
        if not root: return True
        
        def same(lroot, rroot):
    
            if not lroot and not rroot: return True    # both sides empty
            if not lroot or not rroot: return False    # one side missing
            
            if lroot.val != rroot.val: return False
            
            # be careful we want symmetrically same subtrees, not exactly same subtrees
            return same(lroot.left, rroot.right) and same(lroot.right, rroot.left)
            
            
        return same(root.left, root.right)
            
