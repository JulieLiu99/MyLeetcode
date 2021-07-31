"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        """
        BFS
        
        Collect nodes on each level, left to right
        From right to left, point the previous one to the next one
        
        Time O(n)
        Space O(width) = O(4096/2)
        
        """
        if not root: return None
        queue = collections.deque([root])
        
        while queue:
            level = []
            width = len(queue)
            for i in range(width):
                node = queue.popleft()
                level.append(node)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                    
            level[width-1].next = None
            for i in range(width-2, -1, -1):
                level[i].next = level[i+1]
        
        return root
    
    
        """
        Recursion
        
        For each root node of a (sub)tree, create next for its two children:
        
            root.left.next = root.right
            root.right.next = root.next.left (if root.next)
            
        Then move on to its left subtree and right subtree
        
        Time O(n)
        Space O(1)
        
        """
#         if not root:
#             return None
        
#         if root.right:
#             root.left.next = root.right
#             if root.next:
#                 root.right.next = root.next.left
#             else:
#                 root.right.next = None
        
#         self.connect(root.left)
#         self.connect(root.right)
        
#         return root    
