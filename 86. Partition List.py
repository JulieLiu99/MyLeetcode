# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        Dummy head and x_node for the new list
        
        Initialize as:  
                    dummy (smaller) -> x_node (bigger) -> None
        Maintain order while insert:       
                    dummy -> ... -> smaller -> x_node -> ... bigger -> None
        Delete x_node in the end:
                    dummy -> ... -> smaller -> x_node.next -> ... bigger -> None
        
        Time O(n)
        Space O(n)
        
        """
        
        if not head or not head.next: return head
    
        # dummy (smaller) -> x_node (bigger) -> None
        x_node = ListNode(x, None)
        dummy = ListNode(0, x_node)
        smaller = dummy
        bigger = x_node
        
        # dummy -> ... -> smaller -> x_node -> ... bigger -> None
        while head and head.next:
            nextt = head.next
            if head.val < x:
                smaller.next = head
                head.next = x_node
                smaller = smaller.next
            else:
                bigger.next = head
                head.next = None
                bigger = bigger.next
                
            head = nextt
            
        # last one head.next = 0
        if head.val < x:
            smaller.next = head
            head.next = x_node
            smaller = smaller.next
        else:
            bigger.next = head
            head.next = None

        # delete x_node
        smaller.next = x_node.next
        
        return dummy.next
