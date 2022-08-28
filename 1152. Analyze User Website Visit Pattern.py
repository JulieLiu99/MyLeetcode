class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        graph = defaultdict(list)
        for u, t, w in sorted(zip(username, timestamp, website)): # sort by user and time
            graph[u].append(w)
        
        # {'james': ['home', 'cart', 'maps', 'home'], 
        #  'joe': ['home', 'about', 'career'], 
        #  'mary': ['home', 'about', 'career']}
                    
        counter = Counter()
        for username, website in graph.items():
            for triple in set(itertools.combinations(website, 3)):
                counter[triple]+=1
        
        pattern, count = None, 0
        for pat, c in counter.items():
            if c > count:
                pattern = pat
                count = c
            elif c == count and pattern > pat:
                pattern = pat
                
        return pattern
            

