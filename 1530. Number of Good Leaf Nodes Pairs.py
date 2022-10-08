# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        """
        Postorder Traversal
        
        Traverse from bottom to top (postorder) and keep track of the distance of the leaf nodes to each node. 
        """
        res = 0 
        
        def dfs(node):
            nonlocal res
            
            if not node:
                return []
            
            if not node.left and not node.right:
                return [1]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # paths from left leaf to current node to right leaf
            for distance_l in left:
                for distance_r in right:
                    if distance_l + distance_r <= distance:
                        res += 1
                        
            # paths from one side's leaf through current node and go up
            return [length + 1 for length in left + right if length < distance]
        
        dfs(root)
        return res
