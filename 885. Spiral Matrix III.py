class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        '''
        Right 1, Down 1
        Left 2, Up 2
        Right 3, Down 3
        Left 4, Up 4

        O(r * c): Visit the entire board once. Because of the spiral, visit area at most 4x the board.
        '''
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # right, down, left, up
        res = [[rStart, cStart]]
        r, c = rStart, cStart
        steps = 1
        direction_i = 0
        while len(res) < rows * cols:
            for _ in range(2): # increment no. steps every two directions
                dr, dc = directions[direction_i]
                for step in range(1, steps+1):
                    r, c = r + dr, c + dc
                    if 0 <= r < rows and 0 <= c < cols: # cell is on board
                        res.append([r, c])
                direction_i = (direction_i + 1) % 4 # change direction
            steps += 1
        return res