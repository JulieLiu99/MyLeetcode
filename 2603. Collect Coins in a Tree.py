from collections import deque

class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        """
        Topological pruning: BFS naturally processes nodes level by level

        1. Prune all coinless leaves
        2. Trim two layers for distance-2 collections
        3. Count the edges that survive

        Time O(n)
        Space O(n)
        """
        n = len(coins)
        adj = [set() for _ in range(n)]
        deg = [0] * n

        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
            deg[u] += 1
            deg[v] += 1

        # Phase 1: prune all the leaves with no coins
        cleanup = deque([])
        for i in range(n):
            if coins[i] == 0 and deg[i] == 1:
                cleanup.append(i)

        while cleanup:
            node = cleanup.popleft()
            if deg[node] == 0:
                continue
            for neighbor in adj[node]:
                adj[neighbor].remove(node)
                deg[neighbor] -= 1
                if deg[neighbor] == 1 and coins[neighbor] == 0:
                    cleanup.append(neighbor)
            adj[node].clear()
            deg[node] = 0
        
        # Phase 2: remove all the leaves will depth of 2
        for _ in range(2):
            leaves = [i for i in range(n) if deg[i] == 1]
            for node in leaves:
                for neighbor in list(adj[node]):
                    adj[neighbor].remove(node)
                    deg[neighbor] -= 1
                adj[node].clear()
                deg[node] = 0

        
        # Phase 3: count the remaining edges
        edge_count = 0
        for u, v in edges:
            if deg[u] > 0 and deg[v] > 0:
                edge_count += 1
        
        return 2 * edge_count
