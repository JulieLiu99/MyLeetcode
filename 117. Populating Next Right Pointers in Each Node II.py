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
        
        Time O(n)
        Space O(width) 
        
        """
        
        if not root: return None
        
        queue = collections.deque([root])   # to store nodes on each level
        
        while queue:
            width = len(queue)
            level = []
            for i in range(width):
                node = queue.popleft()
                level.append(node)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                    
            for i in range(width-1):
                level[i].next = level[i+1]
        
        return root


        """
        It is just a level order traverse, and we can use a linked list to simulate the queue. 
        Coincidentally, if we store the next pointer in the node itself, then we get the result . 

        Time O(n)
        Space O(1)
        
        """

#         cur = root
#         queue = cur
        
#         while queue:
            
#             cur = queue
#             dummyhead = pre = Node(0) # create a linked list; dummyhead.next is start of one level below cur
            
            
#             while cur:
#                 if cur.left:                    
#                     pre.next = cur.left
#                     pre = cur.left

#                 if cur.right:
#                     pre.next = cur.right
#                     pre = cur.right

#                 cur = cur.next
            
#             queue = dummyhead.next  # go one level down

#         return root
