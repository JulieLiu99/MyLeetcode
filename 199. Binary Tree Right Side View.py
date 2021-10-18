# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Return the last node of each level
        -> BFS

        Time O(n)
        Space O(width)
        
        """
        if not root: return []
        
        q = deque([root])
        res = []
        
        while q:
            
            level = []
            
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                    
            res.append(level[-1])
            
        return res
    
    
        """
        DFS - Postorder
        
        """
        self.res = []
        
        def dfs(root, depth):
            if not root: 
                return
            # meet this `depth` for the first time -> right most node
            if depth == len(self.res): 
                self.res.append(root.val)
            dfs(root.right, depth + 1)  # go right first
            dfs(root.left, depth + 1)
            
        dfs(root, 0)
        return self.res


