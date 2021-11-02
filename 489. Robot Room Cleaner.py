# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        DFS
        
        Manual go back at each step
        Time O(n): visit each cell once, 4 checks per cell
        Space O(n)
        
        """
        visited = set()
        def dfs(x, y, dx, dy):
            # 1, Clean current
            robot.clean()
            visited.add((x, y))

            # 2, Clean next
            for _ in range(4):
                if (x + dx, y + dy) not in visited and robot.move():
                    dfs(x + dx, y + dy, dx, dy)
                robot.turnRight()
                dx, dy = dy, -dx # update direction

            # 3, Back to previous position and direction
            robot.turnRight(); robot.turnRight()
            robot.move()
            robot.turnRight(); robot.turnRight()

        
        dfs(0, 0, 0, 1) # any valid starting point
