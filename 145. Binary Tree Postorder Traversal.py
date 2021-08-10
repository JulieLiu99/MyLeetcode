# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        """
        Recursive
        
        Left subtree, Right subtree, Root
        
        Time O(n)
        Space O(height)
        
        """
        self.res = []
        
        def postorder(root):
            if not root: 
                return
    
            postorder(root.left)
            postorder(root.right)
            self.res.append(root.val)
            
        postorder(root)
        return self.res

        """
        Iterative
        
        Use two stacks:
        
        In stack1:  append left -> right 
                    pop root -> right -> left
        
        In stack2:  append root -> right -> left
                    pop left -> right -> root
        
        Time O(n)
        Space O(n)
        
        """
#         if not root: return []
        
#         stack1 = [root]
#         stack2 = []
#         res = []
        
#         while stack1:
#             node = stack1.pop()
#             stack2.append(node)
            
#             if node.left: 
#                 stack1.append(node.left)
#             if node.right: 
#                 stack1.append(node.right)
        
#         while stack2:
#             res.append(stack2.pop().val)
            
#         return res
