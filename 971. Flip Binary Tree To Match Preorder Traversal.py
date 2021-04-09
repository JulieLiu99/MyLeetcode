# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        """
        Preorder traversal + checking&flipping
        
        Global integer i indicates next index in voyage v.
        If current node == null, it's fine, return true
        If current node.val != v[i], doesn't match wanted value, return false
        If left child exist but don't have wanted value, flip it with right child.
        
        Time O(N)
        Space O(N)
        """
        res = []
        stack = [root]
        i = 0
        while stack:
            node = stack.pop()
            if node.val != voyage[i]: 
                return [-1]
            i += 1
            # if need to swap, append left, right --> pop right first next time
            # this is the same as actually modifying the tree:
            # node.left, node.right = node.right, node.right
            if node.left and node.left.val != voyage[i]:    
                if node.left: 
                    stack.append(node.left)
                if node.right: 
                    stack.append(node.right)
                res.append(node.val)
            # no need to swap, append right, left --> pop left first next time
            else:
                if node.right: 
                    stack.append(node.right)
                if node.left: 
                    stack.append(node.left)
        return res
