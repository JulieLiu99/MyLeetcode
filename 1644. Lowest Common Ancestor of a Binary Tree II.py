# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Postorder DFS
        
        Search from top to bottom, and propogate from bottom to top
        Return bottom-most node that possibly contans both p and q in subtress
        Use countp and counq to check if subtree actually contains p and q
        
        Time O(n)
        Space O(n)
        
        """   
        self.countp = 0
        self.countq = 0
        
        def dfs(root, p, q):
            if not root: 
                return None
            l = dfs(root.left, p, q)
            r = dfs(root.right, p, q)
            if root.val == p.val: 
                self.countp += 1
                return root
            if root.val == q.val: 
                self.countq += 1
                return root
            if l and r: 
                return root
            return l or r  
        
        res = dfs(root, p, q)
        if not self.countp or not self.countq: 
            return None
        return res 
