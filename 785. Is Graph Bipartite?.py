class Solution(object):
    def isBipartite(self, graph):
        """
        BFS + nodes coloring

        Time    O(V+E)
        Space   O(V+E)
        """
        def bfs_bipartite(start):
            q = deque([(start, 1)])
            while q:
                node, color = q.popleft()
                if node in seen:
                    if seen[node] != color:
                        return False
                    continue
                seen[node] = color
                for neighbor in graph[node]:
                    q.append((neighbor, -color))
            return True
    
        seen = {}
        # we need to check every node because it is possible that graph[0] doesn't have any vertices connected
        for i in range(len(graph)):
            if i not in seen:
                if bfs_bipartite(i) == False:
                    return False
        return True

        """
        DFS + nodes coloring

        Time    O(V+E)
        Space   O(V+E)
        """
        def dfs_bipartite(node, color):
            if node in seen:
                if seen[node] != color:
                    return False
                return True
            seen[node] = color
            for neighbor in graph[node]:
                if dfs_bipartite(neighbor, -color) == False:
                    return False
            return True
    
        seen = {}
        # we need to check every node because it is possible that graph[0] doesn't have any vertices connected
        for i in range(len(graph)):
            if i not in seen:
                if dfs_bipartite(i, 1) == False:
                    return False
        return True
