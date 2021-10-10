# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        cur = head
        while cur:
            if cur.val == val: # remove
                pre.next = cur.next
                cur = pre.next
            else:
                pre = cur
                cur = pre.next
        return dummy.next
                
