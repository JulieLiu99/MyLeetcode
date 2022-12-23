class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Brute force: DFS from every node

        Improvement: Result for each node is related to result for parent node. Hence we do not need to do DFS for each node.

        Intuition: While we move down from parent node to current node
        current node sum = parent node sum - 1 * nodes that get closer + 1 * nodes that get further

        2 DFS: 
        One postorder/bottom up that gethers closer_nodes_count (i.e. count of nodes in the subtree) and get sum for root
        One preorder/top down that populate sum for all nodes

        Time O(N)
        Space O(N)

        """
        
        # 1. build graph
        graph = defaultdict(set)

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # 2. initialize variables
        closer_nodes_count = [0] * n
        res = [0] * n

        # 3. 1st DFS
        def dfs1(cur):
            nonlocal closer_nodes_count, res
            subtree_children_count = 0
            for child in graph[cur]:
                if child not in visited:
                    visited.add(child)
                    subtree_children_count += dfs1(child)
            closer_nodes_count[cur] = subtree_children_count + 1 # cur node itself, distance 1 -> 0
            res[0] += subtree_children_count # edges from cur to children have to be added subtree_node_count times
            return subtree_children_count + 1

        visited = set()
        visited.add(0)
        dfs1(0)

        # 4. 2nd DFS
        def dfs2(cur):
            nonlocal res
            for child in graph[cur]:
                if child not in visited:
                    visited.add(child)
                    res[child] = res[cur] - closer_nodes_count[child] + (n - closer_nodes_count[child])
                    dfs2(child)
        
        visited = set()
        visited.add(0)
        dfs2(0)

        return res

