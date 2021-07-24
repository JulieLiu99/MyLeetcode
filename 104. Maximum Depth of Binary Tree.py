# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        """
        BFS
        increment level by 1 after traversing each level
        
        Time O(n)
        Space O(width of tree)
        
        """
        if not root: return 0
        
        level = 0
        queue = collections.deque([root])
        
        while queue:
            width = len(queue)
            for i in range(width):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            level += 1
            
        return level
