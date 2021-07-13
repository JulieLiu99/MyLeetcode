# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        
        """
        0) Dummy node to mark the start
        
        1) Locate the node previous to the left position
        
        2) Reverse till we reach the right position
            each time, reverse from: cur -> nextt -> tmp
                                 to: cur <- nextt -X- tmp
                                 
        3) Connect the three parts of lists 
        
        Time O(n)
        Space O(1)
        
        """

        dummy = ListNode(0, head)

        pre_left = dummy
        for i in range(left-1):
            pre_left = pre_left.next
            
        # each time, reverse between cur and nextt:
        #
        # pre_left -> cur <- nextt -X- tmp -> ...
        #            --------------
        # pre_left -> ... <- cur <- nextt -> temp -> 
        #                   --------------
        #          till cur is at right position
        #       and nextt is start of the ending part
        cur = pre_left.next
        nextt = cur.next
        for i in range(right-left):
            tmp = nextt.next
            nextt.next = cur
            cur = nextt
            nextt = tmp
            
        # connect pre_left to reversed part
        # and reversed part to ending part
        new_left = pre_left.next
        pre_left.next = cur
        new_left.next = nextt
        
        return dummy.next
