"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        """
        The diameter of an N-ary tree is the length of the longest path between any two nodes in the tree
        
        Recursive Postorder Traversal
        
        For Binary Tree:
        Each node returns the max length till its leafs - max(left depth, right depth), where
        Left depth = recursion(node.left) + 1
        Right depth = recursion(node.right) + 1
              
        For N-Ary Tree, 
        Each node returns the max length till its leafs - max([depths of children]), where
        Depth of a child = recursion(node.child) + 1
        
        Keep track of max_path, update with 2 longest depths of children
        
        Time O(n * (#children log #children))
        Space O(n)
        
        """
#         max_path = 0
        
#         def postorder(node):
            
#             nonlocal max_path
            
#             depths = [0, 0]
#             for child in node.children:
#                 depths.append(postorder(child) + 1)

#             depths.sort(reverse = True)
#             max_path = max(max_path, depths[0] + depths[1])

#             return max(depths)
        
#         postorder(root)
#         return max_path


        """
        Get 2 longest depths of children, withouth sorting [depths of children]
        
        Keep top 2 longest depths: max_depth1, max_depth2
        
        max_depth1 is largest, so try to update it first
        Whenever we update max_depth1, update max_depth2 also to the old value of max_depth1 (the now 2nd max value) 
        -> to avoid only updating max_depth1 if depths is an ascending stream
        
        Time O(n)
        Space O(n)
        
        """
    
        max_path = 0
        
        def postorder(node):
            
            nonlocal max_path
            
            max_depth1 = max_depth2 = 0

            for child in node.children:
                depth = postorder(child) + 1
                
                if depth > max_depth1:
                    max_depth1, max_depth2 = depth, max_depth1
                elif depth > max_depth2:
                    max_depth2 = depth

            max_path = max(max_path, max_depth1 + max_depth2)
            
            return max_depth1
        
        postorder(root)
        return max_path
