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
        
        target = head.next
        head.next = None # end of sorted list!!! -> otherwise cycle in the returned list
        while target:
            # find insertion place for target, before head.val > target.val
            while head and head.val <= target.val:
                prev = head
                head = head.next
        
            next_target = target.next
            # insert
            prev.next = target
            target.next = head
            # next target
            target = next_target
            # reinitialize prev and head
            prev = dummy
            head = dummy.next
        
        return dummy.next
