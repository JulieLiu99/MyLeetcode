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
        
        Deque: (node, row, col) down row+1, left col-1, right col+1
        Append col, row, val to a list
        In the end, sort the list, append the vals of the same cols to the same sublist
        
        Time O(n)
        Space O(n)
        
        """
        q = collections.deque([(root, 0, 0)])
        nodes = [(0, 0, root.val)]
        while q:
            for _ in range(len(q)):
                node, row, col = q.popleft()
                if node.left:
                    q.append((node.left, row + 1, col - 1))
                    nodes.append((col - 1, row + 1, node.left.val))
                if node.right:
                    q.append((node.right, row + 1, col + 1))
                    nodes.append((col + 1, row + 1, node.right.val))
                    
        nodes.sort() # sort by col first, then row, then val
        i = 0
        result = []
        while i < len(nodes):
            result.append([nodes[i][2]])
            while i + 1 < len(nodes) and nodes[i + 1][0] == nodes[i][0]: # same col
                result[-1].append(nodes[i + 1][2])
                i += 1
            i += 1
        return result
