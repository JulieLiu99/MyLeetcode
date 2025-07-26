from collections import defaultdict, Counter
from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        # Time O(n log n) + O(m * p^3) + O(p^3)
        # Space O(n) + O(p^3)
        # m: number of users, p: number of websites
         
        user2sites = defaultdict(list)
        for u, t, w in sorted(zip(username, timestamp, website)): # sort by user and time
            user2sites[u].append(w)
        
        # {'james': ['home', 'cart', 'maps', 'home'], 
        #  'joe': ['home', 'about', 'career'], 
        #  'mary': ['home', 'about', 'career']}
                    
        pattern_count = Counter()
        for user, sites in user2sites.items():
            unique_triples = set(combinations(sites, 3))
            for triple in unique_triples:
                pattern_count[triple] += 1
        
        max_pattern, max_count = None, 0
        for pattern, count in pattern_count.items():
            if count > max_count:
                max_pattern = pattern
                max_count = count
            elif count == max_count and max_pattern > pattern:
                max_pattern = pattern
                
        return max_pattern
