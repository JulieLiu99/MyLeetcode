# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        BFS
        
        Go through Tree level by level
        
        1. Keep track of vertical index
            if leftchild, vertical - 1
            if rightchild, vertical + 1
            
        2. Store into dictionary 
            vertical index: node value
            
        3. Keep track of leftmost and rightmost vertial indexes
            append to res column by column from left to right
        
        
        Time O(n)
        Space O(n)
        
        """
        if not root:
            return []
        
        q = deque([(root, 0)])
        vertical_val = {}
        leftmost = 0
        rightmost = 0
        
        while q:
            for _ in range(len(q)):
                node, vertical = q.popleft()
                
                if vertical in vertical_val:
                    vertical_val[vertical].append(node.val)
                else:
                    vertical_val[vertical] = [node.val]
                    
                leftmost = min(leftmost, vertical)
                rightmost = max(rightmost, vertical)
                
                if node.left:
                    q.append((node.left, vertical - 1))
                if node.right:
                    q.append((node.right, vertical + 1))
        
        res = []
        for j in range(leftmost, rightmost + 1):
            res.append(vertical_val[j])
        
        return res
