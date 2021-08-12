# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        Merge Sort Top Down
        
        Time O(nlogn)
        Space O(logn)
        
        """
        
#         if not head or not head.next:
#             return head
        
#         slow = head
#         fast = head.next
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
            
#         start = slow.next
#         slow.next = None
        
#         l, r = self.sortList(head), self.sortList(start)
#         return self.merge(l, r)
        
        
#     def merge(self, l, r):

#         dummy = prev = ListNode(0)
        
#         while l and r:
#             if l.val < r.val:
#                 prev.next = l
#                 l = l.next
#             else:
#                 prev.next = r
#                 r = r.next
#             prev = prev.next
            
#         prev.next = l or r
        
#         return dummy.next
        
    
        """
        Merge Sort Bottom Up
        
        Time O(nlogn)
        Space O(1)
        
        In practice, slighter slower than recursion but uses less memory
        
        """

        def getsize(head):
            size = 0
            while head:
                head = head.next
                size += 1
            return size
        
        def split(head, group_size):    # return head for next group of nodes
            for _ in range(group_size-1):
                if not head:
                    return None
                head = head.next
                
            if not head: return None
            next_head = head.next
            head.next = None
            
            return next_head
        
        def merge(h1, h2, tail):    # return tail for the current merged h1+h2
            while h1 and h2:
                if h1.val <= h2.val:
                    tail.next = h1
                    h1 = h1.next
                else:
                    tail.next = h2
                    h2 = h2.next
                tail = tail.next
                
            tail.next = h1 or h2
            while tail.next:
                tail = tail.next
            return tail
        
        size = getsize(head)
        dummy = ListNode(next=head)
        group_size = 1    # start with pairs of single nodes
        
        while group_size < size:
            tail = dummy
            while head:
                h1 = head
                h2 = split(h1, group_size)
                head = split(h2, group_size)    # head of next round of h1, h2
                tail = merge(h1, h2, tail)      # tail of this round of h1, h2
                                                # we need to keep track of tail because 
                                                # we want to connect merged h1+h2 to the sorted list
            group_size *= 2   # one level up
            head = dummy.next # reinitialize head to the front
            
        return dummy.next
