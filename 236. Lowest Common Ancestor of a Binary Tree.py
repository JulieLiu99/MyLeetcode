# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        """
        Recursion
        Time complexity O(N): worst case visit all nodes due to recursive call 
        Space complexity O(H) or O(N): the height where we find the LCA
        
        
        # If looking for me, return myself
        if root == p or root == q:
            return root
        
        left = right = None
        # else look in left and right child
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)

        # if both children returned a node, means
        # both p and q found so parent is LCA
        if left and right:
            return root
        else:
        # either one of the chidren returned a node, meaning either p or q found on left or right branch.
        # Example: assuming 'p' found in left child, right child returned 'None'. This means 'q' is somewhere below node where 'p' was found. We dont need to search all the way, because in such scenarios, node where 'p' found is LCA
            return left or right
            
        
        """
        
        
        """
        Iteration
        Running time:
        DFS will lead to O(N) since this is a binary tree and not a binary search tree. Two DFS operations will lead to O(N). Comparison work of the lists - using a while loop - to find common element will take O(N)
        So total running time - O(N)

        Space
        Lists to store paths can lead to O(N)
        """
        
        # To find the lowest common ancestor, we need to find where is p and q and a way to track their ancestors. A parent pointer for each node found is good for the job
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
                
        # After we found both p and q, we create a set of p's ancestors. Then we travel through q's ancestors, the first one appears in p's is our answer.
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q
