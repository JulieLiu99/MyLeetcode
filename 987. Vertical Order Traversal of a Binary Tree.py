# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        BFS 
        Save (col, row, value) for each node
        Sort nodes & group by col
        
        Time O(nlogn)
        Space O(n)
        """
        nodes = []
        q = deque([(root, 0, 0)])  # (node, row, col)

        while q:
            node, row, col = q.popleft()
            nodes.append((col, row, node.val))
            if node.left:
                q.append((node.left, row + 1, col - 1))
            if node.right:
                q.append((node.right, row + 1, col + 1))

        nodes.sort()  # sorts by col, then row, then val
        res = []
        prev_col = float('-inf')
        for col, row, val in nodes:
            if col != prev_col:
                res.append([])
                prev_col = col
            res[-1].append(val)
        return res
