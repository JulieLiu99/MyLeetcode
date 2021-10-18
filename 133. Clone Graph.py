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
        
#         if not node: 
#             return
        
#         copy  = {}
#         def dfs(node):
#             copy[node] = Node(node.val)     # copy node
#             for neighbor in node.neighbors: # copy node's neighbors
#                 if neighbor not in copy: 
#                     dfs(neighbor)
#                 copy[node].neighbors.append(copy[neighbor])
                
#         dfs(node)
#         return copy[node]

        """
        BFS
        
        """
        if not node: 
            return
        
        copy = {node : Node(node.val)} # map original nodes to their clones
        q = deque([node])

        while q:
            currNode = q.popleft()
            for neighbor in currNode.neighbors:
                if neighbor not in copy:
                    copy[neighbor] = Node(neighbor.val) # store copy of the neighboring node
                    q.append(neighbor)
                # connect the node copy at hand to its neighboring nodes (also copies) -------- [1]
                copy[currNode].neighbors.append(copy[neighbor])

        # return copy of the starting node ------- [2]
        return copy[node]
