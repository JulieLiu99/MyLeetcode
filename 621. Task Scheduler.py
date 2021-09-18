class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        A A A B B, n=2
        A has max count 3 -> serve as block leader
        [AB_][AB_][A]
        (max_count - 1) blocks of size 3
        A is in final block
        
        A A A B B B, n=2
        A has max count 3 -> serve as block leader
        [AB_][AB_][AB]
        (max_count - 1) blocks of size 3
        B also has max count, so B also appears in final block
        
        A A A B B B C D E F, n=2
        A has max count 3 -> serve as block leader
        [ABC][ABD][ABE][F]
        In this case all tasks can be processed without idle time
        
        Time O(n)
        Space O(n)
        
        """
        
        counter = Counter(tasks)
        max_count = max(list(counter.values()))
                
        res = (max_count - 1) * n + max_count
        
        for task in counter:
            if counter[task] == max_count: 
                res = res + 1  # goes to final block
                
        res -= 1
        
        return max(res, len(tasks))
