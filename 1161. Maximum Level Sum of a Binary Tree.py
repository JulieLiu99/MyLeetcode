# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        BFS
        """
        level = 0
        max_level = 0
        max_sum = float('-inf')
        
        q = collections.deque([root])        
        while q:
            level += 1
            curr_sum = 0
            
            for _ in range(len(q)):
                node = q.popleft()
                curr_sum += node.val
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_level = level
                
        return max_level
