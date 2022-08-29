class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        BFS
        
        Time O(mn)
        Space O(mn)
        
        """
        def bfs(queue):
            while queue:
                i, j = queue.pop()
                if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
                    continue
                grid[i][j] = '#' # mark as visited
                for (new_i, new_j) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    queue.append((new_i, new_j))
        
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1': # start of new island
                    bfs([(i, j)])
                    count += 1
        return count


        """
        DFS
        
        Time O(mn)
        Space O(mn)
        
        """
        
#         def dfs(i, j):
#             if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
#                 return
#             grid[i][j] = '#' # mark as visited
#             for (new_i, new_j) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
#                 dfs(new_i, new_j)

                
#         if not grid:
#             return 0

#         count = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == '1': # start of new island
#                     dfs(i, j)
#                     count += 1
#         return count


