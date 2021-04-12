# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        """
        Min Heap
        
        Insert head of all lists into a priority queue
        
        While pq is not empty:
            pop the top (min)
            insert into answer (dummy head)
            if cur-->next, push to pq
            
        Time O(nk logk)
        Space O(n) + O(k)
        
        k is the number of lists. n is length per list.
        
        heapq is a binary heap, with O(log n) push and O(log n) pop.
        In total nk elements.
        
        The priority queue is aleays size k.
        The answer is size n.
        
        
        """

        dummy = cur = ListNode(0)
           
        heap = []
        for i in range(len(lists)):
            if lists[i]: 
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
                
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            cur.next = node[2]  
            cur = cur.next
            
            if cur.next:
                heapq.heappush(heap, (cur.next.val, idx, cur.next))

        return dummy.next
    

        """
        Divide and Conquer
        
        MergeSort
        
        Time O(nk logk)
        Space O(logk) 
        
        Height of merge tree is logk  
        
        """
        
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)
    
    def merge(self, l, r):
        dummy = cur = ListNode()
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = l or r
        return dummy.next
        
        """
