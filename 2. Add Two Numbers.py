# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        
        uses recursion
        value for current bit: (l1.val + l2.val + i) % 10
        carry for the next bit: (l1.val + l2.val + i) // 10
        
        """
        def rec_fuc(first, second, carry):
            
            if not first and not second and not carry: return None
            
            s = (first.val if first else 0) + (second.val if second else 0) + carry
            node = ListNode(s % 10)
            node.next = rec_fuc(first.next if first else None,
                                second.next if second else None,
                                s // 10)
            return node
        
        return rec_fuc(l1, l2, 0)
            
