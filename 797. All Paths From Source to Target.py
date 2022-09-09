class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        DFS
        Time O(Edges) ~ O(2^n)
        Space O(Nodes) 
        
        """
        def dfs(cur, path):
            if cur == len(graph) - 1: # reached destination: node n-1
                res.append(path)
            else:
                for i in graph[cur]: # nodes that cur leads to
                    dfs(i, path + [i])
        res = []
        dfs(0, [0]) # start from node 0
        return res
