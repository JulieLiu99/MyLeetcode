"""
Skiplist has multiple levels.
Each level is a Sorted Linked List, 
with jump links from current level to elements of the same values in the next level.

Each level has half the size of the next level.
Total space is n + n/2 + n/4 + ... = 2n = O(n)

Time (each operation) O(logn) avg, O(n) worst case
Space O(n) avg, O(nlogn) worst case

"""

import random

class Node:
    def __init__(self, val=-1, right=None, down=None):
        self.val = val
        self.right = right
        self.down = down
        
class Skiplist:

    def __init__(self):
        self.head = Node()  # dummy head

    def search(self, target: int) -> bool:
        node = self.head
        while node:
            # move to the right in the current level till node.right.val >= target or None
            while node.right and node.right.val < target:
                node = node.right
            if node.right and node.right.val == target:
                return True
            # move to the next level
            node = node.down
        return False

    def add(self, num: int) -> None:
        nodes = []  # a list of starting point to insert in each level
        node = self.head
        while node:
            # move to the right in the current level till node.right.val >= target or None
            while node.right and node.right.val < num:
                node = node.right
            nodes.append(node)
            # move to the next level
            node = node.down
            
        insert = True # for sure need to insert into the lowest level
        down = None
        while insert and nodes:
            node = nodes.pop()
            node.right = Node(num, node.right, down)
            down = node.right
            insert = (random.randint(0, 1) == 1)    # divide probability of inserting by 2
            
        # create a new level with a dummy head
        if insert:
            self.head = Node(-1, None, self.head)

    def erase(self, num: int) -> bool:
        node = self.head
        found = False
        while node:
            # move to the right in the current level till node.right.val >= target or None
            while node.right and node.right.val < num:
                node = node.right
            if node.right and node.right.val == num:
                # delete by skipping
                # don't return yet because need to delete num in lower levels
                node.right = node.right.right
                found = True
            # move to the next level
            node = node.down
        return found


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
