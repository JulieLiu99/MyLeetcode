"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        Brute Force: 
            Find all parents of both, 
            then search from top to bottom 
            and return the last commen parent
            -> 3 search
        
        Optimization: 
            Record all parents of one node, 
            then search for parents for the other node 
            and return the first common parent 
            -> 2 search
            
        Time O(n)
        Space O(n)
        
        """
        p_parents = set()
        
        # append all values of p and its parents
        while p:
            p_parents.add(p.val)
            p = p.parent
       
        # loop through all parents and see if there is a common one
        # once found, return
        while q:
            if q.val in p_parents:
                return q
            q = q.parent

        """
        First get depth of both nodes
        Then bring both nodes to same level
        And search for common parent together
        
        Time O(n): worst case 4 search from nodes to root
        Spce O(1)
        
        """
#         def get_depth(node):
#             depth = 0
#             while node.parent:
#                 node = node.parent
#                 depth += 1
#             return depth
#         p_depth = get_depth(p)
#         q_depth = get_depth(q)

#         if q_depth > p_depth:
#             p, q = q, p

#         diff_of_heights = abs(p_depth - q_depth)
#         for _ in range(diff_of_heights):
#             p = p.parent

#         while p != q:
#             p = p.parent
#             q = q.parent

#         return p
