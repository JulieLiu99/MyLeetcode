# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        """
        1. Traverse + Reverse:
        prev -> head -> nextt
                cur
                
        2. Attach
        
        Time O(n)
        Space O(1)
        
        """
        if not head or not head.next: 
            return head
        
        dummy_head = ListNode(next = head)
        pre = dummy_head
        reverse = False
        i = 1
        while True:
            if i == left: # start of reverse
                end_of_first = pre
                start_of_reversed = head
                reverse = True
            if i == right + 1:  # end of reverse
                end_of_reversed = pre
                start_of_third = head
                break
            if reverse:  # prev -> head (cur) -> nextt
                cur = head
                head = head.next
                cur.next = pre
                pre = cur
            else:
                pre = head
                head = head.next
            i += 1
            
        if reverse: # connect starting part -> reversed part -> ending part
            end_of_first.next = end_of_reversed
            start_of_reversed.next = start_of_third
            
        return dummy_head.next
