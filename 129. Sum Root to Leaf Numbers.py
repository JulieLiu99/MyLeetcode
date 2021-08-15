# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        """
        BFS
        
        q stores [node, path]
        
        Time O(n): visit each node once
        Space O(n): q O(width), paths O(width*height)
        
        """
        q = deque([(root, str(root.val))])
        paths = []
        
        while q:
            for _ in range(len(q)):
                node, path = q.popleft()
                if not node.left and not node.right:    # node is leaf
                    paths.append(path)
                if node.left: 
                    q.append((node.left, path+str(node.left.val)))
                if node.right: 
                    q.append((node.right, path+str(node.right.val)))
                
        res = 0
        for path in paths:
            res += int(path)
            
        return res
