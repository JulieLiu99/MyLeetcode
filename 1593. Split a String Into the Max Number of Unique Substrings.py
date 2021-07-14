class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        """
        DFS
        
        Time O(n^2)
        Space O(n^2)
        
        """
        
        used = set()
        n = len(s)
        self.res = 0
        
        def dfs(i, path):
            if i == n:
                self.res = max(self.res, len(path))
                return
            for end in range(i, n):
                if s[i:end+1] not in used:
                    used.add(s[i:end+1])
                    dfs(end+1, path + [s[i:end+1]])
                    used.remove(s[i:end+1])
        
        dfs(0, [])
        return self.res
