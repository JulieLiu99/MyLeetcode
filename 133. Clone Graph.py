"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        DFS - Graph
        
        Time: O(M + N) where N is the number of nodes and M is the number of edges.
        Space: O(N)
        
        """
        
        if not node: 
            return node
        
        copy  = collections.defaultdict(list)
        def dfs(node):
            copy[node] = Node(node.val)     # copy node
            for neighbor in node.neighbors: # copy node's neighbors
                if neighbor not in copy: 
                    dfs(neighbor)
                copy[node].neighbors.append(copy[neighbor])
                
        dfs(node)
        return copy[node]
