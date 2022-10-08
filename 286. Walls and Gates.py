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
        for r in range(rows): 
            for c in range(cols):
                if rooms[r][c] == 0: # bfs from gates
                    q.append((r, c))
        
        # q = [gate0, gate1, gate2, ...their direct neighbor, ... their neighbor's neighbor]
        # guaranteed that unvisited cell gets its distance from the nearest gate
        while q:
            r, c = q.popleft()
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= r+i < rows and 0 <= c+j < cols and rooms[r+i][c+j] == 2147483647: # unvisited neighbor cell
                    rooms[r+i][c+j] = rooms[r][c] + 1 
                    q.append((r+i, c+j))

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
