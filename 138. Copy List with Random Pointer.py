"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        """
        Go over each node in the list and create a copy. 
        If a node has random/next pointer, create random/next pointer for its copy as well.
        Keep track of copied nodes with hashmap {original node: copied node}.
        
        Time O(n)
        Space O(n)
        
        Two Pass
        
        """
        if not head: 
            return 
        
        copied = {}
        node = head
        
        while node != None: # make copy and store in to hashmap
            copied[node] = Node(node.val)
            node = node.next
        
        for node in copied: # assign pointers for the copied nodes
            copy = copied[node]
            if node.next:
                copy.next = copied[node.next]
            if node.random:
                copy.random = copied[node.random]
            
        return copied[head]
        
        """
        Time O(n)
        Space O(n)
        
        One Pass
        
        """
#         if not head:
#             return 
        
#         copied = {head: Node(head.val)}  # original node: copied node
#         node = head

#         while node:
            
#             copy = copied[node]  # copy for current node has already been created as a next node for the previous copy

#             if node.random: 
#                 if node.random not in copied: 
#                     newnode = Node(node.random.val)  # create a copy of node.random
#                     copied[node.random] = newnode    # store to hashmap
#                 copy.random = copied[node.random]    # point from copy of node to copy of node.random

#             if node.next:
#                 if node.next not in copied:          
#                     newnode = Node(node.next.val)    # create a copy of node.next
#                     copied[node.next] = newnode      # store to hashmap
#                 copy.next = copied[node.next]        # point from copy of node to copy of node.next

#             node = node.next
            
#         return copied[head]
