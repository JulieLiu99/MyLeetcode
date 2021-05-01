# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Solution 1
    
    Build Graph (DFS) + Search (BFS)
    
    1. Build a undirected graph (map) from the tree: adjacent_nodes
    2. Traverse the graph from target
    3. Collect all nodes that are K steps from target
    
    Time O(n)
    Space O(n)
    
    """
    
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        adjacent_nodes = collections.defaultdict(list)
    
        def dfs(node, parent_node):
            if parent_node:
                adjacent_nodes[node].append(parent_node)
            if node.left:
                adjacent_nodes[node].append(node.left)
                dfs(node.left, node)
            if node.right:
                adjacent_nodes[node].append(node.right)
                dfs(node.right, node)

        dfs(root, None)

        ans = []
        visited = {target}
        def bfs(node, K):
            if K == 0:
                ans.append(node.val)
            else:
                visited.add(node)
                for adjacent_node in adjacent_nodes[node]:
                    if adjacent_node not in visited:
                        bfs(adjacent_node, K-1)
        bfs(target, K)

        return ans
    
    
    """
    Solution 2
    
    Recursion (Postorder DFS)
    
    1. DFS to build the map that maps a node to its parent.
    2. Traverse the graph from target
    3. Collect all nodes that are K steps from target
    
    Time O(n)
    Space O(n)
    
    """ 
    """ 
    def distanceK(self, root, target, K):

        parentMap = {}
        
        def buildParentMap(node, parent):
            if node is None:
                return
            parentMap[node] = parent
            buildParentMap(node.left, node)
            buildParentMap(node.right, node)
        
        buildParentMap(root, None)
       
        visited = set()
        ans = []
      
        def dfs(node, distance):
            if node is None or node in visited:
                return
            
            visited.add(node)
            
            if distance == K:
                ans.append(node.val)
            elif distance < K:
                dfs(node.left, distance+1)
                dfs(node.right, distance+1)
                dfs(parentMap[node], distance+1)
            # else exceed the scope, no need to explore further
        
        dfs(target, 0)
        
        return ans
    """
