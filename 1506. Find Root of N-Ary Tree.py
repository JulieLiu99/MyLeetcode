"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        """
        We know that the root node is not a child node of any node.
        Add all of the child nodes in a set.
        Root node is the node that is not inside the set.
        
        Time O(n)
        Space O(n)
        
        """
        child_nodes = set()
        
        for node in tree:
            for child in node.children:
                child_nodes.add(child)
        
        for node in tree:
            if node not in child_nodes:
                return node
