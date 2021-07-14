class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        """
        DFS - Recursion
        
        The IPs all have a max length of N = 12
        Time O(N^3)
        Space O(N^3)
        
        """

        n = len(s)
        res = []
        

        def dfs(i, part, path): 

            if i == n:
                if part == 4:
                    res.append(path[:-1])
                    return 
                else:
                    return
            
            if part == 4: 
                return
            
            if i <= n-3 and 0 <= int(s[i:i+3]) <= 255 and s[i] != "0":
                return dfs(i + 3, part + 1, path + s[i:i+3] + ".") or dfs(i + 2, part + 1, path + s[i:i+2] + ".") or dfs(i + 1, part + 1, path + s[i] + ".")

            if i <= n-2 and 0 <= int(s[i:i+2]) <= 255 and s[i] != "0":
                return dfs(i + 2, part + 1, path + s[i:i+2] + ".") or dfs(i + 1, part + 1, path + s[i] + ".")   
            
            return dfs(i + 1, part + 1, path + s[i] + ".")

            
        dfs(0, 0, "")
        return res
