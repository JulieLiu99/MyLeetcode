class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        """
        DFS
        
        Time O(n*2^n): A string with n letters has n-1 gaps. Each gap can be chosen or not chose. e.g. aaaaaa
        Space O(n)
        
        """
        
        res = []
        
        def isPalindrome(s):
            l = 0
            r = len(s) - 1
            while l <= r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
            
        def dfs(s, path):
            if s == "":
                res.append(path)
                return 
            for i in range(len(s)): # can't use range(1, len(s)), s[:i] because single char won't be included
                if isPalindrome(s[:i+1]): 
                    dfs(s[i+1:], path+[s[:i+1]])
            
        dfs(s, [])
        return res
