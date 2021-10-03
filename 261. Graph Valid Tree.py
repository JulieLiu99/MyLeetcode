class Solution:
    
    def buildAdjacencyList(self, n, edges): # a helper function
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        return graph
    
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
    
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        """
        DFS
        
        """
#         graph = self.buildAdjacencyList(n, edges)
#         visited = set([])
#         if self.dfs_cycle(0, -1, graph, visited):
#             return False
#         if len(visited) != n:
#             return False
#         return True
    
#     def dfs_cycle(self, node, parent, graph, visited):
#         visited.add(node)
#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 if self.dfs_cycle(neighbor, node, graph, visited):
#                     return True
#             elif neighbor in visited and neighbor != parent:
#                 return True
#         return False


        """
        BFS
        
        """
        graph = self.buildAdjacencyList(n, edges)
        q = [0]
        visited = set([0])
        parent = [-1] * n  # initialize a parent list
        
        while q:
            node = q.pop(0)      
            for neighbor in graph[node]:
                if neighbor not in visited:
                    parent[neighbor] = node
                    q.append(neighbor)
                    visited.add(neighbor)
                elif neighbor != parent[node]:
                    return False
		
        return len(visited) == n  # If the graph is connected then all vertices must be visited
