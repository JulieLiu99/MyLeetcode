class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        """
        DFS
        Time O(mn)
        Space O(mn)
        """
        m, n = len(maze), len(maze[0])
        visited = set()
        
        def dfs(x, y):
            if (x, y) in visited: 
                return False
            visited.add((x, y))
            if [x, y] == destination:
                return True
            for i, j in [(-1, 0) , (1, 0), (0, -1), (0, 1)]:
                cur_x, cur_y = x, y
                # only change direction when hitting the wall
                while 0 <= cur_x + i < m and 0 <= cur_y + j < n and maze[cur_x + i][cur_y + j] != 1:
                    cur_x += i
                    cur_y += j
                if dfs(cur_x, cur_y):
                    return True
            return False
        
        return dfs(start[0], start[1])
