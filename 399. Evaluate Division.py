class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        Graph 
        precomputation and ad-hoc DFS/BFS
        
        A variation of Floyd–Warshall, computing quotients instead of shortest paths. 
        
        An equation A/B = k is a graph edge A -> B, 
        and (A/B) * (B/C) * (C/D) is the path A -> B -> C -> D.
        
        Time O(equation + query)
        Space O(equation)
        
        """

        quot = collections.defaultdict(dict)
        
        for (num, div), val in zip(equations, values):  # build the graph
            quot[num][num] = 1.0
            quot[div][div] = 1.0
            quot[num][div] = val
            quot[div][num] = 1/val
            
        for k in quot:
            # next two lines same as "for i, j in itertools.permutations(quot[k], 2):"
            for i in quot[k]:       # i connects to k
                for j in quot[k]:   # j also connects to k
                    quot[i][j] = quot[i][k] * quot[k][j]    # connect i -> k -> j
                    
        res = []
        for num, div in queries:
            if num in quot and div in quot[num]:
                res += [quot[num][div]]
            else:
                res += [-1.0]
            
        return res
