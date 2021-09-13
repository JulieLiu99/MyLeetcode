# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """
        Traversal of tree
        If node.val < target: go right
        If node.val > target: go left
        
        Keep track of the current closest val
        
        Time O(logn)
        Space O(1)
        
        """
        if not root:
            return -1
        
        closest = root.val
                
        while(root):
            
            if (abs(target-root.val) < abs(target-closest)):
                closest = root.val

            if target < root.val:
                root = root.left
            else:
                root = root.right
            
        return closest  
