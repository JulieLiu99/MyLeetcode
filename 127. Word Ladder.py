class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        BFS
        
        First build the adjacency graph: 
            using collections.defaultdict(list)
            Time O(n * m^2):    where n is len(wordList) and m is len(endWord)
                                for each word (n)
                                * replace every char to get a pattern (m)
                                and add word to neighbors[pattern] (m)
            Space O(n* m)
        
        Then BFS traverse the graph layer by layer: 
            until we reach the endWord or can't go anymore
            Time O(n^2 * m):    at most visit each word once (n)
                                find all patterns of each word (m)
                                try all neighbors in neighbors[pattern] (n)
        
            Space O(n)
            
        """
        
        if endWord not in wordList:
             return 0
            
        neighbors = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                neighbors[pattern].append(word)
                       
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord: # we've reached endWord
                    return res      # -> return number of layers
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for neighbor in neighbors[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
            if not q and word != endWord:   # if no more next layer but still not reached endWord 
                return 0                    # -> failure
            res += 1
        
        return res


	"""
        BFS
        
        Time O(L * 26 * n): L is length of word, n is size of wordList
        Space O(n)
         
        """
        wordList = set(wordList)
        q = collections.deque([[beginWord, 1]])
        
        while q:
            word, length = q.popleft()
            
            if word == endWord:
                return length
            
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz': # try all replacements
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word) # don't revisit
                        q.append([next_word, length+1])
                        
        return 0