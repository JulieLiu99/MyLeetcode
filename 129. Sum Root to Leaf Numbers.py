# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        Preorder Traversal
        
        If left: cur += left.val
        If right: cur += right.val
        
        Before return to node, remove last char in cur
        
        Time O(n)
        Space O(n)
        
        """
        if not root: return
        
        nums = []
        
        def preorder(node, cur):

            cur += str(node.val)
    
            if not node.left and not node.right: # leaf, num is complete
                nums.append(int(cur))
                return 
            
            if node.left: preorder(node.left, cur)
            if node.right: preorder(node.right, cur)
            
        preorder(root, "")
        return sum(nums)
