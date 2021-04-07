# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        preorder: root, [left...], [right...]
        inorder: [left...], root, [right...]
        preorder --> inorder: find index of root in inorder
        
        list.pop(0) takes O(n) time because all elements have to be shifted
        """
        
        """
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root
        """
        """
        Use list.pop(0) instead, which costs O(1)
        
        Time O(n^2) 
        Space O(n^2) 
        
        still not much faster
        
        """
        def build(preorder, inorder):
            if inorder:
                ind = inorder.index(preorder.pop())
                root = TreeNode(inorder[ind])
                root.left = build(preorder, inorder[0:ind])
                root.right = build(preorder, inorder[ind+1:])
                return root
        preorder.reverse()
        return build(preorder, inorder)
