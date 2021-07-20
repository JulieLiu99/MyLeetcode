# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Recursion
        
        Time O(n)
        Space O(n)
        
        """
        
        self.res = []
        
        def inorder(root):
            
            if root.left:
                inorder(root.left)
            
            if root:
                self.res.append(root.val)
            else:
                return
            
            if root.right:
                inorder(root.right)
            
        if root:
            inorder(root)
        
        return self.res

    
        """
        Iteration
        
        Time O(n)
        Space O(n)
        
        """

#         res = []
#         stack = []
        
#         while True:
#             if root:
#                 stack.append(root)
#                 root = root.left
#             elif stack:
#                 root = stack.pop()
#                 res.append(root.val)
#                 root = root.right
#             else:
#                 break
    
#         return res
