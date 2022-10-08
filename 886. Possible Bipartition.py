class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        """
        Think of graph, node coloring, and DFS.

        Abstract model transformation:

        A person is Node.

        P1 and P2 dislike each other: Node1 and Node2 share one edge, and they need two different colors {1, -1}.

        If we can draw each dislike pair with two different colors {1, -1}, then there exists at least one possible bipartition.
        
        Time O(E+V) 
        Space O(E+V)
        """
        def dfs(person, color):                
            if person in colored:
                return color == colored[person]
            colored[person] = color        
            for hate in graph[person]:                
                if not dfs(hate, color * -1):
                    return False
            return True
    
        # build graph
        graph = collections.defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        # color n people (labeled from 1 to n)  
        colored = {}  
        for person in range(1, n+1):  
            if person not in colored and not dfs(person, 1): # new cluster
                return False
            
        return len(colored) == n # all colored
