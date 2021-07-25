# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
            
        """
        
        We cannot just use 
        
        if not root:
            return 0
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        
        because this would preterminate the depth search before reaching a leaf -> falsely return 1
        
        2
         \
          3
           \
            4
             \
              5
               \
                6
                
        Time O(n)
        Space O(n)
        
        """

        if not root:
            return 0
        
        if root.left and root.right:    # still not leaf node yet: children on both sides
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        elif root.left:                 # sill not leaf node yet: children on the left
            return 1 + self.minDepth(root.left)
        elif root.right:                # still not leaf node yet: children on the right
            return 1 + self.minDepth(root.right)
        else:                           # current root is leaf node
            return 1

        """
        Just another way of writing the same thing
        surprisingly a bit slower
        
        """
#         def find(root):
#             if not root.left and not root.right:  # current root is leaf node
#                 return 1
            
#             if root.left and root.right:
#                 return 1 + min(find(root.left), find(root.right))
#             elif root.left:
#                 return 1 + find(root.left)
#             elif root.right:
#                 return 1 + find(root.right)
        
#         if not root: 
#             return 0
#         return find(root)
