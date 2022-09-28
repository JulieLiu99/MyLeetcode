class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        """
              [[0,0],[0,1],
         [1,0],      [1,2],     --> one by one can remove 5 stones
               [2,1],[2,2]]
               
        The whole problem can be translated to:
        What is the number of islands?
        
        One island must have at least one stone left.
        Maximum number of stones removed = total - number of islands (number of remaining stones).

        Time O(n)
        Space O(n)
        """
        def dfs(i, j): # explore entire island
            for new_j in rows[i]: # all cells in the same row
                if (i, new_j) not in seen:
                    seen.add((i, new_j))
                    dfs(i, new_j)
            for new_i in cols[j]: # all cells in the same col
                if (new_i, j) not in seen:
                    seen.add((new_i, j))
                    dfs(new_i, j)
                    
        rows, cols = collections.defaultdict(list), collections.defaultdict(list)
        for i,j in stones:
            rows[i].append(j)
            cols[j].append(i)
            
        seen = set()
    
        islands = 0
        for i,j in stones:
            if (i, j) not in seen:
                islands +=1
                dfs(i, j)
        return len(stones) - islands
