class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        """
        DFS 
        
        Time O(nk)
        Space O(nk)
        
        """
        # optimization - handle larger task first
        jobs.sort(reverse = True)
        
        n = len(jobs)
        count = [0 for _ in range(k)] 
        self.res = float('inf')
        
        def dfs(i, curMaxTime):
            
            # optimization - no need to continue if curMaxtime is bigger than minimum
            if curMaxTime >= self.res:
                return self.res
            
            if i == n:
                self.res = min(self.res, curMaxTime)
                return
            
            seen = set()
            for worker in range(k):
                # optimization - no need to try a worker in the same situation as the previous one 
                if count[worker] not in seen:
                    count[worker] += jobs[i]
                    dfs(i+1, max(curMaxTime, count[worker]))
                    count[worker] -= jobs[i]
                    
                    seen.add(count[worker])
                    
        dfs(0, 0)
        return self.res
