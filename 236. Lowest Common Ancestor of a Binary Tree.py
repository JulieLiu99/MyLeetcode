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
        Return bottom-most node that contans both p and q in subtress
        
        Time O(n)
        Space O(n)
        
        """
        def dfs(root, p, q):
            if not root: 
                return None
            l = dfs(root.left, p, q)
            r = dfs(root.right, p, q)
            if root.val == p.val or root.val == q.val: 
                return root
            if l and r: 
                return root
            return l or r  
        
        return dfs(root, p, q)

    
#         # 1. Search from top to bottom
#         # if found bottom-most ancester, no need to go down further, start propagating
#         # if reached the bottom, propagate not found
        
#         if not root: return 
            
#         if root == p or root == q:
#             return root

#         ancestorLeft = self.lowestCommonAncestor(root.left, p, q)
#         ancestorRight = self.lowestCommonAncestor(root.right, p, q)

#         # 2. Propogate from bottom to top
        
#         # If found ancestorLeft and ancestorRight below root, propagate root 
#         # (which later might be propated up as ancestorLeft/ancestorRight)
#         if ancestorLeft and ancestorRight:
#             return root

#         # If ancestorLeft contains pq, while ancestorRight contains nothing, propagate ancestorLeft
#         if ancestorLeft:
#             return ancestorLeft

#         # If ancestorRight contains pq, while ancestorLeft contains nothing, propagate ancestorRight
#         if ancestorRight:
#             return ancestorRight

#         else: 
#             return 
