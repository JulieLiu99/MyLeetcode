class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        Backtracking DFS
        
        Time O(n^2): for every starting point, O(n) ending point
        Space O(n^3): O(n^2) for recursion stack, each time storing string s
        
        """
#         wordDict = set(wordDict)
#         res = []
        
#         def dfs(s, path):
#             if s == "":
#                 res.append(path[:])
#             else:
#                 for i in range(1, len(s)+1):
#                     if s[:i] in wordDict: # substring can match with a word
#                         path.append(s[:i])
#                         dfs(s[i:] ,path)
#                         path.pop() # if not successful, remove substring from path
        
#         dfs(s, [])
#         return [" ".join(path) for path in res]


        """
        Space Optimization

        Space O(n^2): instead of passing string, pass index

        """
        wordDict = set(wordDict)
        res = []

        def dfs(i, path):
            if i == len(s):
                res.append(path[:])
            else:
                for j in range(i, len(s)+1):
                    if s[i:j+1] in wordDict: # substring can match with a word
                        path.append(s[i:j+1])
                        dfs(j+1 ,path)
                        path.pop() # if not successful, remove substring from path

        dfs(0, [])
        return [" ".join(path) for path in res]
