class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        Topological Sort (using Adjacency Graph and DFS Search)
        
        Strings in words are sorted lexicographically by the rules of this new language
        
        Return a string of the unique letters in the new alien language sorted in lexicographically increasing order
        
        -> LinkedList/ Non Cyclic Graph
        -> If a letter points to a previous letter, cycle, wrong

        Time O(n)
        Space O(n)
        
        """
        adj = {c: set() for w in words for c in w}
        # build adjacency graph
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]: # corner wrong case
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:  # w1[j] < w2[j] in our dictionary
                    adj[w1[j]].add(w2[j]) # put first different char into adj graph
                    break

        visited = {} # False = visited, True = in current path, shouldn't be pointed back
        res = []
        def dfs_cycle(c):
            if c in visited:
                return visited[c] # if in current path already -> cycle -> False

            visited[c] = True   # include it into current path, shouldn't be pointed back
            for nextt in adj[c]:
                if dfs_cycle(nextt):  # cycle back to anywhere from c till nextt
                    return True
            visited[c] = False
            res.append(c)
            return False

        for c in adj:
            if dfs_cycle(c):
                return ""

        res.reverse()
        return "".join(res) 
