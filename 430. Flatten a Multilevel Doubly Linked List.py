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
        
        while current:
            # check for child node
            if current.child:
                # merge child list into the parent list
                self.merge(current)
                
            # move to the next node
            current = current.next
        
        return head
            
    
    def merge(self, current):
        child = current.child
        
        # traverse until the last node of the child list
        while child.next:
            child = child.next
        
        # connect child.next to current.next, if there is any
        if current.next:
            child.next = current.next
            current.next.prev = child
        
        # connect current to the child list
        current.next = current.child
        current.child.prev = current
        
        # remove self.child pointer
        current.child = None