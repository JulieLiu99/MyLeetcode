# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        Preorder Traversal
        
        If current node within range -> add to res
        If it's larger than low -> go to right
        If it's smaller than high -> go to left
        
        Time O(high - low)
        Space O(high - low)
        
        """
        self.res = 0

        def preorder(node: Optional[TreeNode]):
            
            if low <= node.val <= high:
                self.res += node.val
                
            if node.left and node.val > low:
                preorder(node.left)
                
            if node.right and node.val < high:
                preorder(node.right)
            
            return
        
        if root:
            preorder(root)
        else:
            return 0
        
        return self.res
