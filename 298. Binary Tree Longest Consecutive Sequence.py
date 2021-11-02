# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        """
        Recursive DFS
        
        """
        def postorder(root):
            nonlocal max_length
            if not root:
                return 0
            
            l = postorder(root.left)
            r = postorder(root.right)
            
            length = 1 # just root node
            if root.left and root.left.val == root.val + 1: # root node + left path
                length = max(length, 1 + l)
            if root.right and root.right.val == root.val + 1: # root node + right path
                length = max(length, 1 + r)
                
            max_length = max(max_length, length)
            return length
        
        max_length = 0
        postorder(root)
        return max_length

        """
        Iterative DFS
        
        """
        if not root: return 0
        stack = [(root, 1)]
        max_length = 1
        while stack:
            node, length = stack.pop()
            max_length = max(max_length, length)
            for child in (node.left, node.right):
                if not child: continue
                if child.val == node.val + 1:
                    stack.append((child, length + 1)) # root node + child path
                else:
                    stack.append((child, 1)) # just root node
        return max_length 
