class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        Backtracking DFS
        
        Time O(n^2): for every starting point, O(n) ending point
        Space O(n^3): O(n^2) for recursion stack, each time storing string s
        
        """
        wordDict = set(wordDict)
        res = []
        
        def dfs(s, path):
            if s == "":
                res.append(path[1:]) # discard initial space
            else:
                for i in range(len(s)):
                    if s[:i+1] in wordDict: # substring can match with a word
                        dfs(s[i+1:] ,path+" "+s[:i+1])
        
        dfs(s, "")
        return res


        """
        Space Optimization

        Space O(n^2): instead of passing string, pass index

        """
        # wordDict = set(wordDict)
        # res = []
        # def dfs(i, path):
        #     if i == len(s):
        #         res.append(path[1:]) # ignore initial space
        #     else:
        #         for j in range(i, len(s)+1):
        #             if s[i:j+1] in wordDict:
        #                 dfs(j+1, path + " " + s[i:j+1])
        # dfs(0, "")
        # return res
        
#         memo = {}
#         def dfs(s):
#             if s in memo: 
#                 return memo[s]
#             res = []
#             for i in range(1, len(s)+1):
#                 if s[:i] in wordDict: # substring can match with a word
#                     word = s[:i]
#                     if s[i:]: # if more left
#                         tails = dfs(s[i:])
#                         for tail in tails:
#                             res.append(word + " " + tail)
#                     else:
#                         res.append(word)
#             memo[s] = res
#             return res
        
#         return dfs(s)
    
#         memo = {}
#         def dfs(s):
#             if s in memo: 
#                 return memo[s]
#             if not s: 
#                 return []

#             res = []
#             for word in wordDict:
#                 if not s.startswith(word):
#                     continue
#                 if len(word) == len(s):
#                     res.append(word)
#                 else:
#                     tails = dfs(s[len(word):])
#                     for tail in tails:
#                         res.append(word + ' ' + tail)
#             memo[s] = res
#             return res
        
#         return dfs(s)

