# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iterative
        
        prev -> head -> next -> ...
                cur    
                
        """
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev
    
        """
        Recursive
        
        head -> head.next (reversed aleady from here on)
        
        """
        # if not head or not head.next:
        #     return head
        # node = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return node
