# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return
        
        dummy_node = ListNode()
        l3 = dummy_node
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry

            carry = total//10
            l3.next = ListNode(total%10)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            l3 = l3.next
        
        return dummy_node.next

        # def rec_fuc(first, second, carry):
            
        #     if not first and not second and not carry: return None
            
        #     s = (first.val if first else 0) + (second.val if second else 0) + carry
        #     node = ListNode(s % 10)
        #     node.next = rec_fuc(first.next if first else None,
        #                         second.next if second else None,
        #                         s // 10)
        #     return node
        
        # return rec_fuc(l1, l2, 0)
