"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        """
        Sorted in ascending order
        
        Time O(n)
        Space O(1)
        
        """
        
        node = Node(insertVal) 
        
        if not head:  # list is empty -> create a circular list
            node.next = node
            return node
        
        curr = head
        while curr.next:
            
            # coming to the end -> insert at the end
            if curr.next == head: 
                node.next = curr.next 
                curr.next = node 
                return head
            
            # found place in middle of ascending nodes, or
            # at the end of ascending nodes, before the min starting node
            if (curr.val <= insertVal <= curr.next.val) or ((curr.val > curr.next.val) and (insertVal >= curr.val or insertVal <= curr.next.val)):
                node.next = curr.next 
                curr.next = node
                return head
            
            curr = curr.next
        
        return head
