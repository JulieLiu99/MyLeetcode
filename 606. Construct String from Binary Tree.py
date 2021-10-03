# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        """
        Iterative - Stack
        
        """
#         if not root: 
#             return ""
        
#         stack = [root]
#         res = ""
        
#         while stack:
#             node = stack.pop()
#             if node == ")":
#                 res += ")"
#             else:
#                 res += "(" + str(node.val)
                
#                 if not node.left and node.right:
#                     res += "()"
#                 if  node.right:
#                     stack.append(")")
#                     stack.append(node.right)
#                 if  node.left:
#                     stack.append(")")
#                     stack.append(node.left)

#         return res[1:]
    
    
        """
        Recursive
        
        """
    
        if not root:
            return ""
        
        res = ""
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        
        if left or right: # if not left, "()"
            res += "(" + str(left) + ")"
        if right:
            res += "(" + str(right) + ")"
            
        return str(root.val) + res
