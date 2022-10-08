"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        
        """
        the left pointer of the tree node should point to its predecessor, 
        and the right pointer should point to its successor.
        
        predecessor <-left-- node --right-> successor
        
        Time O(n)
        Space O(n)
        
        """
#         if not root:
#             return None
        
#         self.list = []
        
#         self.inorder(root)
        
#         # the left pointer of the tree node should point to its predecessor, 
#         for i in range(1, len(self.list)):
#             self.list[i].left = self.list[i-1]
         
#         # and the right pointer should point to its successor.
#         for i in range(0, len(self.list)-1):
#             self.list[i].right= self.list[i+1]
        
#         # the predecessor of the first element is the last element, 
#         self.list[0].left = self.list[-1]
        
#         # and the successor of the last element is the first element.
#         self.list[-1].right = self.list[0]
        
#         return self.list[0]
    
#     def inorder(self,root):
#         if not root:
#             return
#         self.inorder(root.left)
#         self.list.append(root)
#         self.inorder(root.right)

        """
        Inorder Recursion, Link in place
        
        Time O(n)
        Space O(1)
        
        """
        if not root:
            return

        dummy = Node()
        self.prev = dummy

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.prev.right = node
            node.left = self.prev
            self.prev = node
            inorder(node.right)

        inorder(root)
        dummy.right.left = self.prev    # when inorder traversal completes, self.prev is last/right most node
        self.prev.right = dummy.right
        
        return dummy.right
