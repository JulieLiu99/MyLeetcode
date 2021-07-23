# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        DSF
        
        Important to use floor and ceiling
        And constantly update them!!!
        
        e.g. 2 is invalid 
             because it is not only supposed to be < than its parent 4,
             but also > than all the previous nodes up to the root.
        5
         \
          4
         /  \
        2    6
        
        Time O(n)
        Space O(n)
        
        """
	
        def check(node, floor, ceiling):
            if not node:
                return True

            if not floor < node.val < ceiling:
                return False

            return check(node.left, floor, node.val) and check(node.right, node.val, ceiling)
        
        return check(root, float("-inf"), float("inf"))
