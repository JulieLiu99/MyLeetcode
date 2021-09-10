class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        """
        'S': player
        'B': box
        'T': target
        
        '.': free cell to walk
        '#': impossible to walk 
        
        1 BFS for searching for possible next move, until box hits target
        1 BFS for checking if player can get to the position and do this move to box
        
          P  B        in order to push B to next position,
             |
             V

          A-->P
          |            P needs to go above B first. And after the push, P will be where B used to be.
          P   B
          
        Time O(n^2)
        Space O(n)
        
        """        
        # check if player can move from start to next pushing position given ball's current position
        def can_move(start, end, ball):
            if 0 <= end[0] < rows and 0 <= end[1] < cols:
                q = collections.deque([start])
                seen = {start}
                while q:
                    row, col = q.popleft()
                    if (row, col) == end:  # hit the goal -> valid path
                        return True
                    for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        player_x, player_y = row + i, col + j
                        if 0 <= player_x < rows and 0 <= player_y < cols and grid[player_x][player_y] != '#' and (player_x, player_y) != ball and (player_x, player_y) not in seen:
                            seen.add((player_x, player_y))
                            q.append((player_x, player_y))
            return False

        rows, cols = len(grid), len(grid[0])

        # find positions of target, player, ball
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'T':
                    target = (r, c)
                elif grid[r][c] == 'S':
                    player = (r, c)
                elif grid[r][c] == 'B':
                    ball = (r, c)

        # bfs starting from current positions of player, ball
        seen = {(player, ball)}
        q = collections.deque([(0, player, ball)])

        while q:
            pushes, player, ball = q.popleft()

            if ball == target: # hits the target, pushes is guaranteed to be the minimum possible
                return pushes

            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ball_x, ball_y = ball[0] + i, ball[1] + j  # next position for box

                if 0 <= ball_x < rows and 0 <= ball_y < cols and grid[ball_x][ball_y] != '#':
                    push_pos = (ball[0] - i, ball[1] - j)  # player's pushing position

                    if (ball, (ball_x, ball_y)) not in seen and can_move(player, push_pos, ball):
                        seen.add((ball, (ball_x, ball_y)))
                        q.append((pushes + 1, ball, (ball_x, ball_y)))

        return -1
