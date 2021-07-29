class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        """
        Priority Queue
        
        Sort projects by their capital requirements, small to big, and keep project indexes
        
        For each capital amount I have (w):
            Maintain a heap of all available projects, sorted by profits large to small
            Pop the project with max profit and update w
        
        Time O(nlogn)
        Space O(n)
        
        """
        
        capital = sorted([(c, i) for i, c in enumerate(capital)])   # smallest capital to largest
        pq = [] # to store available projects, sorted from max profit to min profit
        
        i = 0
        chosen = 0
        n = len(profits)
        
        while chosen < k:

            while i < n and capital[i][0] <= w:        # add all available projects
                heappush(pq, -1 * profits[capital[i][1]])
                i += 1

            if pq: 
                w -= heappop(pq)  # do this project: -= instead of += because we stored negative profits in pq
                chosen += 1
            else:
                break   # no available projects

        return w
