# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Binary Search
    
    Compare the depth between left sub tree and right sub tree:
    
    - If equal --> current tree is a full binary tree
        2**leftDepth-1
        
    - If not equal --> keep searching one level down
        1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    Time O(log n * log n):
    - Each time to find depth we need O(log n) - height of tree. 
    - We need O(log n) binary search - width of tree.
    
    Space O(log n)
    
    """
    
    # 1 get depth recursively through helper functions
    
    """
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftDepth = self.getLeftDepth(root)
        rightDepth = self.getRightDepth(root)
        if leftDepth == rightDepth:
            return 2**leftDepth - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def getLeftDepth(self, root):
        if not root:
            return 0
        return 1 + self.getLeftDepth(root.left)
    
    def getRightDepth(self, root):
        if not root:
            return 0
        return 1 + self.getRightDepth(root.right)
   """
    
    # 2 get depth iteratively through while loop
    
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        leftDepth = rightDepth = 0
        
        node = root
        while node:
            leftDepth += 1
            node = node.left
            
        node = root
        while node:
            rightDepth += 1
            node = node.right
            
        if leftDepth == rightDepth: # subtree is a complete tree
            return 2**leftDepth-1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
