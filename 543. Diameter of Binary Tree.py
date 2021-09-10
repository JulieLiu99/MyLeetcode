# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        """
        DFS (postorder: left right root)
        
        Get depth from left and right side through recursion
        
        Update res: depth from left + depth from right
        
        Return max depth below this root -> used as left and right for parent of this root
        
        Time O(n)
        Space O(n)
        
        """
        
        if not root: return
        
        self.res = 0
        
        def dfs(root):
            
            left = right = 0
            
            # start from bottom
            if root.left:
                left = dfs(root.left)
            if root.right:
                right = dfs(root.right)

            # update res: diameter = max left depth + max right depth
            self.res = max(self.res, left + right) 

            # max depth of this root: serves as child depth for its parent
            # from this root to its parent node(1) + max depth of this root
            return 1 + max(left, right) 
        
        dfs(root)
        return self.res
