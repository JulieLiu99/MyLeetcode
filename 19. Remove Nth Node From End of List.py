# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        # Go through list and get length, then remove length-n-1
        # Time O(n)
        # Space O(n)
        
        nodes = []
        pos = head
        while pos is not None:
            nodes.append(pos)
            pos = pos.next
        L = len(nodes)
        if n == L:
            if L > 1:
                return nodes[1]
            else:
                return None
        else:
            index = L-n-1
            nodes[index].next = nodes[index+1].next
            return head
