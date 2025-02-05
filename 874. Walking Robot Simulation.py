class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """
        Direction list + Obstable set

        Time O(n + m): n is number of commands, m is number of obstacles
        Space O(m)
        """

        x, y = 0, 0
        res = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d = 0
        obstacles = {tuple(o) for o in obstacles}

        for c in commands:

            if c == -1: # turn right
                d = (d + 1) % 4

            elif c == -2: # turn left
                d = (d - 1) % 4

            else: # move forward
                dx, dy = directions[d]
                for step in range(c):
                    if (x + dx, y + dy) in obstacles:
                        break
                    x, y = x + dx, y + dy

            res = max(res, x**2 + y**2)

        return res