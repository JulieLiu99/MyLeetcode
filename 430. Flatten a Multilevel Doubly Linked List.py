"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        """
        Iterative
        
        Time O(n): each node gets visited at most twice - once as child, once as flattened
        Space O(1)
        
        """
        current = head
        
        while current is not None:
            # check for child node
            if current.child is not None:
                # merge child list into the parent list
                self.merge(current)
                
            # move to the next node
            current = current.next
        
        return head
            
    
    def merge(self, current):
        child = current.child
        
        # traverse until the last node of the child list
        while child.next is not None:
            child = child.next
        
        # connect child.next to current.next, if there is any
        if current.next is not None:
            child.next = current.next
            current.next.prev = child
        
        # connect current to the child list
        current.next = current.child
        current.child.prev = current
        
        # at the end remove self.child pointer
        current.child = None
