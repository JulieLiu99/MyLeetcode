# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """
        BFS
        
        For each horizontal layer, find the maximum
        
        Time O(n)
        Space O(width)
        
        """
        if not root: return []
        
        q = deque([root])
        res = []
        while q:
            layer_max = float("-inf")
            for _ in range(len(q)):
                node = q.popleft()
                layer_max = max(layer_max, node.val)
                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(layer_max)
            
        return res
