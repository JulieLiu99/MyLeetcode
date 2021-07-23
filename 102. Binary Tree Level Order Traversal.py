# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        Iterative BFS
        While loop + Queue
        
        Time O(n)
        Space O(MaxWidth of Tree)
        
        """
        
        if not root: return []
        
        queue = collections.deque([root])
        res = []
        
        while queue:

            cur_level = []
            width = len(queue) # width of previous level
            
            for i in range(width): 
                node = queue.popleft()
                cur_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            res.append(cur_level)
            
        return res

