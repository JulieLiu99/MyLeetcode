class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        BFS from gates
        
        Time O(nm)
        Space O(nm)
        
        """
        if not rooms: # edge case
            return []
        
        rows = len(rooms)
        cols = len(rooms[0])
        q = collections.deque()
        for r in range(rows): # bfs from gates
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= r+x < rows and 0 <= c+y < cols and rooms[r+x][c+y] == 2147483647:
                    rooms[r+x][c+y] = rooms[r][c] + 1 # update neighbors, if they are not visited
                    q.append((r+x, c+y))

        """
        DFS - TLE
        
        With DFS, we cannot take advantage of that fact that if a room is not 2147483647, it's been visited by the nearest gate already.
        
        Time O(nm)
        Space O(nm)
        
        """
#         def dfs(rooms, r, c, step):
#             for x, y in [(-1,0), (1,0), (0,-1), (0,1)]:
#                 if 0 <= r+x < len(rooms) and 0 <= c+y < len(rooms[0]) and rooms[r+x][c+y] > rooms[r][c]:
#                     rooms[r+x][c+y] = step + 1
#                     dfs(rooms, r+x, c+y, step+1)
        
#         if not rooms: # edge case
#             return []
#         for r in range(len(rooms)):
#             for c in range(len(rooms[0])):
#                 if rooms[r][c] == 0: # dfs from gates
#                     dfs(rooms, r, c, 0)
