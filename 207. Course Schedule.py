class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Topological Sorting, Directed Graph, DFS
        
        Can't have circle
        
        Time O(n^2)
        Space O(n^2)
        
        """
        G = {i:set() for i in range(numCourses)}
        for nextt, pre in prerequisites:
            G[pre].add(nextt)
            
        visit = [0] * numCourses
        
        def dfs_circle(x):
            visit[x] = -1 # visiting
            for y in G[x]:
                if visit[y] < 0 or (not visit[y] and dfs_circle(y)):
                    return True
            visit[x] = 1 # visited
            return False
        
        for x in range(numCourses):
            if not visit[x]:
                if dfs_circle(x):
                    return False
        return True
