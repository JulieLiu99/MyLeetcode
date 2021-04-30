# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
DFS + Recursion

Time O(n)
Space O(n)

Instead of creating new path, which is a costly operation,
Directly manipulate on the original path using backtracking.

[]
if not root.left and not root.right:
   if sum == root.val:
       path.append(root.val)
       result.append(path)

self.dfs(root.left, sum - root.val, result, path + [root.val])
self.dfs(root.right, sum - root.val,result,  path + [root.val])

"""
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        result = []
        self.dfs(root, targetSum, result, [])
        return result 

    def dfs(self, root, targetSum, result, path):
        if not root:
            return 

        path.append(root.val)

        if not root.left and not root.right: # leaf node
            if root.val == targetSum:
                # for primitive values, [:] is sufficient (although it is doing shallow copy)
                result.append(path[:])
                
        self.dfs(root.left, targetSum-root.val, result, path)
        self.dfs(root.right, targetSum-root.val, result, path)

        # backtrack 
        # pop before going back up to the parent node to check the right side of the tree
        path.pop()
