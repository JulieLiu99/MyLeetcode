# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        """
        Recursion
        
        Time O(n^2)
        Space O(n^2)
        
        """
        
        def generate(l, r):   # split between [l, r)
            
            if l == r:
                return [None]
            
            nodes = []
            
            for root in range(l, r):
                for lchild in generate(l, root):
                    for rchild in generate(root+1, r):
                        node = TreeNode(root+1)   # +1 to convert the index to the actual value
                        node.left = lchild
                        node.right = rchild
                        nodes += [node]
                        
            return nodes
        
        return generate(0, n) 
