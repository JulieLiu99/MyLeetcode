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
           
        # (max_count-1) full buckets of size n+1
        res = (max_count-1) * (n+1) 
        
        for task in counter:
            if counter[task] == max_count: 
                res += 1  # goes to final bucket
        
        # there could be a variety of tasks at the end
        return max(res, len(tasks))
