class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
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
            
            
        Difference from 127. Word Ladder:
        
        1. Need to return all shorted paths instead of length of path
           -> res = [] instead of res = 0
              res.append(path) instead of res += 1
              
        2. Queue stores (neighbor, path+[neighbor])
           So that when we pop, we also have the path
           word, path = q.popleft()
              
        3. Only update visited at end of current layer 
           visited = visited.union(localVisited)
           Because we can revisit the same word in the same layer but from different paths

        """
        
        if endWord not in wordList:
            return []

        neighbors = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                neighbors[pattern].append(word)

        # Shortest path, BFS
        res = []
        q = deque([(beginWord, [beginWord])])
        visited = set([beginWord])

        while q and not res:
            # only update visited at end of current layer 
            # because we can revisit the same word 
            # in the same layer but from different paths
            localVisited = set()    
            for _ in range(len(q)):
                word, path = q.popleft()
                # the first layer to reach endWord (because res[] is empty till this layer)
                # record all paths that can reach endWord in this layer
                if word == endWord:         
                    res.append(path)  
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for neighbor in neighbors[pattern]:
                        if neighbor not in visited:
                            localVisited.add(neighbor)
                            q.append((neighbor, path+[neighbor]))
            visited = visited.union(localVisited)
            
        return res
