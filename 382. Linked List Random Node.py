# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    """
    Reservoir Sampling
    
    Brute force:
    First traverse list and get size
    return value of position random.randint(0, size)
    
    With a stream (unknown size) of values: Reservoir Sampling
    e.g.to randomly pick one out of [a,b,c,d]
    x = a
    x = 1/2 x, 1/2 b => 1/2 a, 1/2 b
    x = 2/3 x, 1/3 c => 1/3 a, 1/3 b, 1/3 c
    x = 3/4 x, 1/4 d => 1/4 a, 1/4 b, 1/4 c, 1/4 d
    
    Time O(n)
    Space O(1)
    
    """

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        count = result = 0
        cur = self.head
        while cur:
            count += 1
            if random.random() <= 1/count:  # change to new val
                result = cur.val
            cur = cur.next  
        return result


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
