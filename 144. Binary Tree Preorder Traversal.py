# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Recursion
        
        Process root (if empty return)
        Process left and right subtrees
        
        Time O(n)
        Space O(height)
        
        """
                
        self.res = []
        
        def preorder(root):
            if root:
                self.res.append(root.val)
            else:
                return
            
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        return self.res

        """
        Iterative
        
        Use stack to store subtree
        
        Append right subtree before left
        In order to pop left before right
        
        Keep popping the left child while it exists, and simultaneously,
        push the right child of every node in an auxiliary stack. 
        
        Once we reach a null node, pop a right child from the auxiliary stack 
        and repeat the process while the auxiliary stack is not-empty.
        
        Time O(n)
        Space O(height)
        
        """
    
#         if not root: return []
        
#         stack = [root]
#         res = []
        
#         while stack:
#             node = stack.pop()
#             res.append(node.val)
            
#             if node.right: stack.append(node.right)
#             if node.left: stack.append(node.left)
            
#         return res
