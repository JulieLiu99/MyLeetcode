# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Convert both lists to nums
    Then convert sum to list
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.list_to_num(l1)
        num2 = self.list_to_num(l2)
        
        return self.num_to_list(num1 + num2)
    
    def list_to_num(self, node):
        num = 0
        while node:
            num = num * 10 + node.val
            node = node.next
        return num
    
    def num_to_list(self, num):
        # none <- 3 
        # none <- 3 <- 2
        # none <- 3 <- 2 <- 1
        if num == 0: 
            return ListNode(0)
        tail = None
        while num:
            node = ListNode(num % 10)
            node.next = tail
            tail = node # move tail to current node
            num //= 10             
        return tail

        """
        Reverse both lists
        Then add two lists from least significant digit
        """
#         l1, l2 = self.reverseList(l1), self.reverseList(l2)
#         tail = None
#         carry = 0
#         while l1 or l2 or carry:
#             if l1:
#                 carry += l1.val
#                 l1 = l1.next
#             if l2:
#                 carry += l2.val
#                 l2 = l2.next
#             prev = ListNode(carry%10)
#             prev.next = tail
#             tail = prev
#             carry //= 10

#         return prev


#     def reverseList(self, head): # 7 -> 2 -> 4 -> 3 -> none TO none <- 7 <- 2 <- 4 <- 3
#         tail = None
#         while head:
#             prev = head.next
#             head.next = tail
#             tail = head 
#             head = prev
#         return tail
