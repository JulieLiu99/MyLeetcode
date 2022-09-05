# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Preorder: [root, left branch, right branch]
                    ^
        Inorder:  [left branch, root, right branch]
                                 ^idx
        Time O(n^2): O(n) calls, each O(n) time from index and slicing
        Space O(n^2): O(n) calls, each O(n) space from slicing
        
        """
        """
        Directly pass in sliced preorder and inorder
        """
        
#         if not preorder or not inorder:
#             return 
    
#         root = TreeNode(preorder[0])
#         idx = inorder.index(preorder[0])
#         root.left = self.buildTree(preorder[1: idx+1], inorder[:idx])
#         root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
#         return root

        """
        Treat preorder as mutable object
        
        In Python, if a mutable object is passed as a function parameter, its value is adaptive to recursive calls; while if an immutable object is passed as a function parameter, its value is fixed to every recursive call.
            
        Here list - preorder - is mutable.
        """
        
        if inorder:
            # get root from front of inorder list
            root_val = preorder.pop(0)
            root = TreeNode(root_val)
            
            # split preorder list into left and right branch 
            idx = inorder.index(root_val)
            root.left = self.buildTree(preorder, inorder[0:idx])    
            root.right = self.buildTree(preorder, inorder[idx+1:])
            return root
