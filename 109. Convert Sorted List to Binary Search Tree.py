# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        
        """
        Recursion - Binary DFS
        
        Time O(n): n nodes being created once for each
        Space O(logn): recursive head
        
        """
        
        if not head: return None
        prev = dummy = ListNode(0, head)
        slow = fast = head
        
        while fast: 
            if fast.next:
                fast = fast.next.next
            else:
                break
            prev = slow
            slow = slow.next
            
        # slow is mid, or start of second half
        mid = TreeNode(slow.val)
        prev.next = None
        mid.left = self.sortedListToBST(dummy.next) # can't use head!!! will never be None!!! mid can be head!!!
        mid.right = self.sortedListToBST(slow.next)
        
        return mid
