# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        """
        Mark all visited nodes: node.val = [node.val]
        
        Time O(n)
        Space O(1)
        
        """
#         while head:
            
#             if type(head.val) == list:   # reached a previously visited node
#                 head.val = head.val[0]
#                 return head
            
#             head.val = [head.val]
#             head = head.next
            
#         return 

        """
        Brute Force
        
        Store all visted nodes
        
        Time O(n)
        Space O(n)
        
        Surprisingly even better space performance in practice
        
        """

#         if not head: return
    
#         visited = set([head])
#         while head.next:
#             if head.next in visited:
#                 return head.next
#             visited.add(head.next)
#             head = head.next
            
#         return
        
        """
        Fast and Slow Pointers
        
        1. we wait until fast pointer gains slow pointer.
        2. move slow pointer and head with the same speed until they concide.
          
        *---m---*----p---*| MEET HERE
                \        /               
                 \______/   
                    m
                    
        n is length of cycle
        
        Fast: m + k_f * n + p
        Slow: m + k_s * n + p
        
        m + k_f * n + p = 2 * (m + k_s * n + p)
                k_f * n = 2 * k_s * n + m + p
                  m + p = n
                  
        Time O(kn):  we traverse our linked list twice
        Space O(1)
        
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        while head != slow:
            slow = slow.next
            head = head.next
        return head
