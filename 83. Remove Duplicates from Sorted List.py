# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        """
        Iterative solution
        Dummy head
        
        Time O(n)
        Space O(1)
        
        """
        
        if head == None or head.next == None: return head
        
        dummy = ListNode(0, head)
        
        while head and head.next:
            nextt = head.next

            # head is start of duplicate
            if head.val == nextt.val:
                duplicate_val = head.val
                while nextt and nextt.val == duplicate_val:
                    nextt = nextt.next  
                head.next = nextt

            head = nextt
        
        return dummy.next
