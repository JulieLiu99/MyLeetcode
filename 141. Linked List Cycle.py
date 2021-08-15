# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Brute Force
        Go through the list
        Record all visited nodes
        If come across the same node -> return True
        
        * Can't only keep node.val -> moving forward, might come across a different node with same val 
        
        Time O(n)
        Space O(n)
        
        """
#         if not head: 
#             return False
        
#         seen = set([head])

#         while head.next:
#             if head.next in seen:
#                 return True
#             else:
#                 seen.add(head.next)
#                 head = head.next
                
#         return False

        """
        Optimization: 
        
        Instead of recording all visited nodes, mark all visted nodes as None
        
        Time O(n)
        Space O(1)
        
        """
        while head:
            
            if head.val == None:    # we have visited this node before
                return True
            
            head.val = None
            head = head.next
            
        return False
