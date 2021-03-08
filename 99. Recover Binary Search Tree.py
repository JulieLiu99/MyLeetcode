# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.res = []

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        
        adjacent swap:   1, 2, 4, 3, 5 --> 4, 3
        inadjacent swap: 1, 2, 5, 4, 3 --> 5, 4, 3
        
        Time O(n)
        Space O(n)
        """
        
        self.mid(root)
        node1 = None
        node2 = None
        
        for i in range(len(self.res)-1):
            
            if self.res[i].val > self.res[i+1].val and node1 == None:
                node1 = self.res[i]
                node2 = self.res[i+1]
                
            elif self.res[i].val > self.res[i+1].val and node1 != None:
                node2 = self.res[i+1]
                
        node1.val, node2.val = node2.val, node1.val
        
    # left first traversal --> res[] nodes in ascending order
    def mid(self,root):
        if root is not None:
            self.mid(root.left)
            self.res.append(root)
            self.mid(root.right)
