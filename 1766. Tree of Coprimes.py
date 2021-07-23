class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        """
        
        1. Convert list of edges to a graph
        2. Use graph to make a map parent_graph[node] = nodes_parent
        3. For each node walk up the parent_graph to find an ancestor with gcd(node_val, ancestor_val) = 1
        
        
        Because we are walking up the graph, we will search the same ancestors many times over.
        Add memoization to the find_ancestor function to reduce redundant computations.
              8
             / 
            6   
           /
          4   
         / \
        2   2

        The left 2 will walk all the way up to the root before it realizes there are no ancestors with a GCD of 1.
        The right 2 can stop as soon as we reach 4 because it has the same value as the other 2 and this path was explored already.

        """
        
        # Convert edges to a graph
        graph = collections.defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        # Find the parent of each node
        parent_graph = collections.defaultdict(int)
        level = [(0, -1)]
        while level:
            next_level = []
            for node, parent in level:
                parent_graph[node] = parent
                for neighbor in graph[node]:    # connecting nodes that aren't parent
                    if neighbor != parent:      # = neighbors of a lower level
                        next_level.append((neighbor, node))
            level = next_level

        @lru_cache(None)
        def find_ancestor(node, node_value):
            '''Returns the closest ancestor with a GCD of 1 if one exists.  Otherwise return -1.'''
            if node == -1:
                return -1
            parent = parent_graph[node]
            if math.gcd(node_value, nums[parent]) == 1:
                return parent
            return find_ancestor(parent, node_value)
        
        # Find the nearest ancestor for each node that has a GCD of 1
        return [find_ancestor(node, nums[node]) for node in range(len(nums))]
