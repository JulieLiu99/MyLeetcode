# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        """
        While loop
        First clean the front and find the distinct val head
        Then loop through and remove duplicates in place
            
        Time O(n)
        Space O(1)
        
        Works but not fast
        
        """
        
#         if head == None or head.next == None: return head
        
#         start_from_next = False
        
#         # head is duplicate
#         if head.next.val == head.val:
#             while head.next and head.next.val == head.val:
#                 head = head.next
#             if head.next == None: return None
#             # head.next.val != head.val
#             # dummy_head = head instead of head.next bc
#             # we know head is the last of the same val
#             dummy_head = head
#             start_from_next = True
#         else:
#             dummy_head = head
            
#         while head.next and head.next.next:
#             cur = head.next
#             nextt = cur.next
            
#             # cur is start of duplicate
#             # head is last single val
#             if cur.val == nextt.val:
#                 while nextt and cur.val == nextt.val:
#                     nextt = nextt.next
#                 if nextt == None: # duplicates till the end
#                     head.next = None
#                 else:   # next is the first different val
#                     head.next = nextt
#             else:
#                 head = cur
        
#         if start_from_next:
#             return dummy_head.next
#         return dummy_head

        """
        Dummy head prior to head
        
        --> solve the issue of having a distinct pre-node
            so that we can remove from there
        
        """

        dummy = pre = ListNode(0)
        dummy.next = head
        
        while head and head.next:
            
            # head is start of duplicate
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next    # first different val
                pre.next = head
    
            else:
                pre = pre.next
                head = head.next
                
        return dummy.next
