class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        # Time O(nlogn) + O(m p!) + O(p!)
        # Space O(n) + O(m) + O(p!)
        # m: number of users, p: number of websites
         
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
        
        max_pattern, max_count = None, 0
        for pattern, count in counter.items():
            if count > max_count:
                max_pattern = pattern
                max_count = count
            elif count == max_count and max_pattern > pattern:
                max_pattern = pattern
                
        return max_pattern
