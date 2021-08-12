# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        For each insertion, loop new element through the existing sorted list
        
        Time O(n^2)
        Space O(1)
        
        Pretty good performance
        
        """
        
        dummy = prev = ListNode()
        dummy.next = head
        
        nextt = head.next
        head.next = None # end of sorted list!!! -> otherwise cycle in the returned list
        while nextt:
            # find insertion place for nextt, before head.val > nextt.val
            while head and head.val <= nextt.val:
                prev = head
                head = head.next
        
            next_target = nextt.next
            # insert
            prev.next = nextt
            nextt.next = head
            # next target
            nextt = next_target
            # reinitialize prev and head
            prev = dummy
            head = dummy.next
        
        return dummy.next
