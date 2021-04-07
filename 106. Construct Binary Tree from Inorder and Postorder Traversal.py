# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        """
        inorder: [left..], root, [right..]
        postorder: [left..], [right..], root
        
        Time O(N^2)
        Space O(N^2)
        for balanced tree we have O(N*LnN)
        
        """
        
        map_inorder = {}    # instead of list.index(..) which takes O(N)
        for i, val in enumerate(inorder): map_inorder[val] = i
            
        def build(low, high):
            if low > high: 
                return None
            root = TreeNode(postorder.pop())
            idx = map_inorder[root.val]
            root.right = build(idx+1, high)
            root.left = build(low, idx-1)
            return root
        
        return build(0, len(inorder)-1)
