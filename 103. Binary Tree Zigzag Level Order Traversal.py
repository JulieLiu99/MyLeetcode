# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        """
        Maintain a reverse indicator
        
        For each level, either res.append(level) or res.append(reversed(level))
        
        Time O(n)
        Space O(width of tree)
        
        """
                
        if not root: return []
        
        res = []
        queue = collections.deque([root])
        reverse = -1
        
        while queue:
            level = []
            width = len(queue)
            
            for i in range(width):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                    
            if reverse == -1:
                res.append(level)
            else:
                res.append(reversed(level))
            reverse *= -1
            
        return res
    
    
    
        """
        This is not right!!!
        
        [1,2,3,4,null,null,5]
          1
         / \
        2   3
        \    \
         4    5
        outputs                     [[1],[3,2],[5,4]]
        when it's supposed to be    [[1],[3,2],[4,5]]
        
        This is because 3 gets appended to and popped from queue prior to 2,
        and thus 5 comes before 4 even we don't want reversed level here.
        
        """
#         if not root: return []
        
#         res = []
#         queue = collections.deque([root])
#         reverse = 1
        
#         while queue:
#             level = []
#             width = len(queue)
            
#             for i in range(width):
#                 node = queue.popleft()
#                 level.append(node.val)
#                 if reverse == 1:
#                     print("!!reverse!!", node.left, node.right)
#                     if node.right: queue.append(node.right)
#                     if node.left: queue.append(node.left)
#                 else:
#                     print(node.left, node.right)
#                     if node.left: queue.append(node.left)
#                     if node.right: queue.append(node.right)
                        
#             res.append(level)
#             reverse *= -1
            
#         return res
