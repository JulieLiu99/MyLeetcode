# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        """
        Time O(n)
        Space O(1)
        
        """
        if not head: return
        
        # count length of list and get tail
        node = head
        n = 1
        while node.next:
            n += 1
            node = node.next
        tail = node
        
        # [0,1,2] 4
        if k >= n: k %= n
        if n == 1 or k == 0: return head
        
        # get new tail and head
        node = head
        for _ in range(n-k-1):
            node = node.next
            
        # node now the tail to be
        new_head = node.next
        node.next = None
        tail.next = head
        
        return new_head
