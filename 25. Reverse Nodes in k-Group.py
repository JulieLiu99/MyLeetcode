# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        """
        Use a dummy head, and

        l, r : define reversing range

        pre, cur : used in reversing, standard reverse linked linked list method

        jump : used to connect last node in previous k-group to first node in following k-group
        
        Time O(n) 
        Space O(1) 
        
        """
        
        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            count = 0
            
            # use r to locate the range
            while r and count < k:   
                r = r.next
                count += 1
                
            # if size k satisfied, reverse the inner linked list
            if count == k:  
                pre, cur = r, l
                for _ in range(k):
                    # reverse
                    temp = cur.next
                    cur.next = pre
                    pre = cur
                    cur = temp
                    
                    # k = 3 for example:
                    #
                    #        cur temp  pre
                    # init  : a -> b -> c -> (next k-group)
                    #
                    #            cur  temp
                    # step 0:      b -> c -> (next k-group)
                    #                   a ---^
                    #                  pre
                    #
                    #                  cur  temp
                    # step 1:           c -> (next k-group)
                    #              b -> a ---^
                    #             pre
                    #
                    # step 2:                (next k-group)
                    #         c -> b -> a ---^
                    #        pre        
                    #                   l
                    # finish: c -> b -> a -> (next k-group)
                    
                # connect two k-groups
                jump.next = pre
                jump = l
                l = r
            else:
                return dummy.next
