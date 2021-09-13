# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        """
        Two Recursive Traversals
        
        Inorder traversal --> sorted array
        Sorted array --> BST
        
        Time O(n)
        Space O(n)
        
        """
#         values = []
#         self.inorder(root, values)
#         new_root = self.construct_BST(values)
#         return new_root
        
#     def inorder(self, root, values):
#         if not root:
#             return 
#         self.inorder(root.left,values)
#         values.append(root.val)
#         self.inorder(root.right,values)
        
#     def construct_BST(self, values):
#         if not values:
#             return
        
#         mid = (len(values)-1)//2
#         node = TreeNode(values[mid])
        
#         node.left = self.construct_BST(values[0:mid])
#         node.right = self.construct_BST(values[mid+1:])
#         return node


        """
        Iterative Inorder Traversal (instead of recursion)
        
        Much faster
        
        """
    
        stack = []
        inorder = []
        node = root
        while True:
            if node:
                stack.append(node)
                node = node.left
            elif stack:
                node = stack.pop()
                inorder.append(node)
                node = node.right
            else:
                break
                
        def create_balanced_tree(ls):
            if not ls:
                return None
            
            mid = (len(ls)-1)//2
            root = ls[mid]
            root.left = create_balanced_tree(ls[:mid])
            root.right = create_balanced_tree(ls[mid+1:])
            
            return root
        
        return create_balanced_tree(inorder)
