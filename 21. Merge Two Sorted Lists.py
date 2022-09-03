# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Merge iteratively
        Time O(n)
        Space O(1)
        """
        # dummy = cur = ListNode(0)
        # while l1 and l2:
        #     if l1.val < l2.val:
        #         cur.next = l1
        #         l1 = l1.next
        #     else:
        #         cur.next = l2
        #         l2 = l2.next
        #     cur = cur.next
        # cur.next = l1 or l2
        # return dummy.next
    
        
        """
        Without creating new dummy node
        """
#         if not l1 or not l2:
#             return l1 or l2
        
#         seek, target = (l1, l2) if l1.val < l2.val else (l2, l1)
#         head = seek
        
#         while seek and target:
#             while seek.next and seek.next.val < target.val:
#                 seek = seek.next
#             seek.next, target = target, seek.next
#             seek = seek.next
            
#         return head
    
        """
        Recursively
        """
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2