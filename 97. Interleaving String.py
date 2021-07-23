class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        """
        DFS
        
        Time complexity is O(n1 * n2), because we have n1 * n2 states and two transactions from one state to others. 
        Space complexity is O(n1 * n2) as well.
        
        """
        
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        
        if n1 + n2 != n3: return False
                
        @lru_cache(None)
        def dfs(i1, i2, i3):
            
            if i3 == n3: return True
            
            if (i1 < n1 and s1[i1] == s3[i3]) and (i2 < n2 and s2[i2] == s3[i3]):
                return dfs(i1+1, i2, i3+1) or dfs(i1, i2+1, i3+1)
                
            elif i1 < n1 and s1[i1] == s3[i3]:
                return dfs(i1+1, i2, i3+1)
            
            elif i2 < n2 and s2[i2] == s3[i3]:
                return dfs(i1, i2+1, i3+1)
            
            return False
            
        return dfs(0, 0, 0)
