class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """
        DP
        
        """
        res = []
        preWords = set()
        
        # asc order of word length, since longer words are formed by shorter words
        words.sort(key = len)
        
        # for each short word start building preWords
        for word in words:
            if self.wordBreak(word, preWords):
                res.append(word)
            preWords.add(word)
        
        return res
    
    # Word Break I template
    def wordBreak(self, string, words):
        if not words:
            return False
        
        dp = [False] * (len(string) + 1)
        dp[0] = True
        
        for i in range(len(string)+1):
            for j in range(i):
                if dp[j] and string[j:i] in words:
                    dp[i] = True
                    break
        
        return dp[-1]
    
        """
        DFS + memorization
        TLE
        
        Time O(N * L^3): O(L^2) sub-problems, each sub problem O(L) because slicing creates a new string
        
        """
        # d = set(words)
        # memo = {}
        # def dfs(word):
        #     if word in memo:
        #         return memo[word]
        #     memo[word] = False
        #     for i in range(1, len(word)):
        #         prefix = word[:i]
        #         suffix = word[i:]
        #         if prefix in d and suffix in d:
        #             memo[word] = True 
        #             return True
        #         if prefix in d and dfs(suffix):
        #             memo[word] = True 
        #             return True
        #         if suffix in d and dfs(prefix):
        #             memo[word] = True 
        #             return True
        #     return False
        # return [word for word in words if dfs(word)] 
