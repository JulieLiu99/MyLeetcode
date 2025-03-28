# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        """
        Postorder traversal
        Delete node: Return None to parent's call
                        node.left = dfs(node.left)
                        node.right = dfs(node.right)
        Return roots: Add children as roots whenever parent node is deleted

        Time O(n)
        Space O(n)
        """
        to_delete = set(to_delete)
        res_set = set([root])

        def dfs(node):
            if not node:
                return None
            res = node
            if node.val in to_delete:
                # parent tree ends here
                res = None
                res_set.discard(node)
                if node.left: 
                    # new tree
                    res_set.add(node.left) 
                if node.right: 
                    # new tree
                    res_set.add(node.right)
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return res

        dfs(root)
        return list(res_set)