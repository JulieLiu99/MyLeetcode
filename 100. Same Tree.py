# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        """
        Traverse both trees together
        
        Time O(n)
        Space O(n)
        
        """
        
        # two trees have to end together
        if not p and not q: return True
        if not p: return False
        if not q: return False
        
        if p.val != q.val: return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
