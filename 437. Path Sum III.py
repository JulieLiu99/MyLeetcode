# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Brute Force: from each node, try all sub paths possible, time O(n^2)
    
    Memorization of path sum
    'Space and time tradeoff'
    
    Create a dictionary to save all path sums (root -> current node) and their frequency
    If there is a valid subpath: currPathSum - targetSum = existingPathSum
    Number of valid subpaths: sum_count[currPathSum - targetSum]
    
    Time O(n) because just one traverse
    Space O(n)
    
    """
    def pathSum(self, root: TreeNode, targetSum: int) -> int:

        self.result = 0
        sum_count = defaultdict(int)
        sum_count[0] = 1 # for subpath starting from root where currPathSum = targetSum
        
        # recursively get result
        self.dfs(root, targetSum, 0, sum_count)
        return self.result
    
    def dfs(self, root, targetSum, currPathSum, sum_count):
    
        if root is None: # exit condition
            return  
        
        currPathSum += root.val
        
        self.result += sum_count[currPathSum - targetSum]
        sum_count[currPathSum] = sum_count[currPathSum] + 1
        
        # dfs breakdown
        self.dfs(root.left, targetSum, currPathSum, sum_count)
        self.dfs(root.right, targetSum, currPathSum, sum_count)
        # when move to a different branch, the currPathSum is no longer available, hence remove one. 
        sum_count[currPathSum] -= 1
