# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Phase 1: Reverse the first half while finding the middle.
        Phase 2: Compare the reversed first half with the second half.
        
        Time O(n)
        Space O(1)
        
        """
        fast = slow = head
        pre = None

        # find the middle node (slow) and reverse nodes in first half
        while fast and fast.next:
            fast = fast.next.next # move fast
            current = slow
            slow = slow.next # move slow
            current.next = pre # reverse
            pre = current

        if fast:  # list has odd nodes, middle is slow.next
            slow = slow.next

        # check if pre equals slow
        while pre:
            if pre.val != slow.val:
                return False
            pre = pre.next # to front
            slow = slow.next # to end

        return True

        """
        Deque: pop from both left and right
        
        Time O(n)
        Space (n)
        
        """
        # queue = collections.deque([])
        # cur = head
        # while cur:
        #     queue.append(cur)
        #     cur = cur.next
        # while len(queue) >= 2:
        #     if queue.popleft().val != queue.pop().val:
        #         return False
        # return True
