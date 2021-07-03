# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        
        Time O(n): first do O(n) iterations to find middle, then O(n) iterations to reverse second half and finally O(n) iterations to merge lists. 
        
        Space O(1).
        
        """
        # step 1: find middle 
        # [1,2,3,4,5]           [1,2,3,4]
        #      ^   ^               ^ ^
        if not head: return []
        mid = head  # either mid, or left to mid
        end = head  # either last, or second to last
        while end.next and end.next.next:
            mid = mid.next
            end = end.next.next
        
        # step 2: reverse second half
        # [1,2,3,4,5]           [1,2,3,4]
        #       [5,4]               [4,3]
        prev = None
        current = mid.next
        while current:
            nextt = current.next
            current.next = prev # reverse link
            prev = current
            current = nextt    
        mid.next = None
        
        # step 3: merge lists
        # [1,5,2,4,3]           [1,4,2,3]
        #    ^   ^                 ^   ^ 
        head1 = head
        head2 = prev    # last node
        while head2:
            nextt = head1.next
            head1.next = head2  # add in second half
            head1 = head2
            head2 = nextt
