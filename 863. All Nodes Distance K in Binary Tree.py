# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Build Graph + DFS
    
    1. Build undirected graph through preorder traversal 
    2. BFS from target node to search for nodes K steps away
    
    Time O(N)
    Space O(N)
    
    """ 
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        graph = collections.defaultdict(list)
        def preOrder(node):
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                preOrder(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                preOrder(node.right)
                
        preOrder(root)
        
        # # BFS for k steps
        # level = [target.val]
        # seen = set(level)
        # for _ in range(k):
        #     new_level = []
        #     for node in level:
        #         for neighbor in graph[node]:
        #             if neighbor not in seen:
        #                 new_level.append(neighbor)
        #                 seen.add(neighbor)
        #     level = new_level
        # return level
                
        #DFS
        seen = set()
        res = []
        def dfs(node, step):
            if step == k:
                res.append(node)
                return
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    dfs(neighbor, step+1)
            seen.remove(node)

        dfs(target.val, 0)
        return res


