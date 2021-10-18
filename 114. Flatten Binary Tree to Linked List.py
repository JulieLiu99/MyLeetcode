# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        """
        DFS Recursion
        
        Time O(n)
        Space O(n): height of tree, O(n) as doesn't say about tree being balanced or not 
N. 
        
        """
#         def dfs(node):
#             if not node: 
#                 return 

#             if not node.left and not node.right: # leaf
#                 return node

#             leftTail = dfs(node.left)
#             rightTail = dfs(node.right)

#             if leftTail:
#                 leftTail.right = node.right
#                 node.right = node.left
#                 node.left = None

#             return rightTail if rightTail else leftTail

#         dfs(root)
        
        """
        Iteration
        
        Time O(n)
        Space O(1)
        
        """
        if not root:
            return 
        
        node = root
        while node:
            
            if node.left:
                
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right
                
                # rewire the connections
                rightmost.right = node.right
                node.right = node.left
                node.left = None
            
            # move on to next node in the linked list
            node = node.right
