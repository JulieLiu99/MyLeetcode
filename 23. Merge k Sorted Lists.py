# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Divide-and-Conquer 
        
        Time O(nlogn)
        Space O(n)
        
        """
#         def merge(l1, l2):
#             dummy = ListNode()
#             cur = dummy
#             while l1 and l2:
#                 if l1.val <= l2.val:
#                     cur.next = l1
#                     cur = l1
#                     l1 = l1.next
#                 else:
#                     cur.next = l2
#                     cur = l2
#                     l2 = l2.next
#             cur.next = l1 if l1 else l2
#             return dummy.next
        
#         n = len(lists)
#         if n == 0:
#             return None
#         if n == 1:
#             return lists[0]
#         mid = n//2
#         l1 = self.mergeKLists(lists[:mid])
#         l2 = self.mergeKLists(lists[mid:])
#         return merge(l1, l2)


        """
        Heap
        
        Time O(nlogk)
        Space O(k)
        
        Note: push (node.val, i, node) to heap
        i is there so that node does not get involved into heat sorting
        when node.val of two items are the same, i resolves the comparison
        
        """
        dummyhead = pre = ListNode()
        q = []
        i = 0
        for l in lists:
            if l:
                heapq.heappush(q, (l.val, i, l))
                i += 1
        while q:
            val, _, node = heapq.heappop(q)
            pre.next = node
            pre = node
            if node.next:
                heapq.heappush(q, (node.next.val, i, node.next))
                i += 1
        return dummyhead.next