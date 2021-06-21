class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        DFS + backtracking
        
        board[i][j]
        9 rows, key: i
        9 cols, key: j
        9 squares, key: i//3*3 + j//3
        e.g. board[4][6] is in square 4//3*3 + 6//3 = 3 + 2 = 5
        
        row, col, square to record states.
        9 * 9 because for each cell, could be of value 1~9.
        True means cell is not filled with value, Flase means filled with one specific vale.
        For each empty cell, try 1~9.
        
        Time O(9^n): for each cell try 9 different options
        Space O(n)
        
        """
        row = [[True]*9 for i in range(9)]        
        col = [[True]*9 for i in range(9)]
        square = [[True]*9 for i in range(9)]  # 3*3 sub-square, from left to right, top to bottom.
        to_fill = []
        for i in range(9):
            for j in range(9):
                # already filled
                if board[i][j] != '.':
                    d = int(board[i][j]) - 1
                    row[i][d] = col[j][d] = square[i//3*3+j//3][d] = False
                # to be filled
                else:
                    to_fill.append((i, j))

                    
        def backtrack():
            if not to_fill: 
                return True
            
            i, j = to_fill.pop()
            for d in range(9):
                # can fill in with this value
                if row[i][d] and col[j][d] and square[i//3*3+j//3][d]:
                    board[i][j] = str(d+1)
                    row[i][d] = col[j][d] = square[i//3*3+j//3][d] = False
                    # there is valid solution
                    if backtrack():
                        return True
                    # reverse to original
                    board[i][j] = '.'
                    row[i][d] = col[j][d] = square[i//3*3+j//3][d] = True
            
            # if no value from 0~9 worked for this cell -> no solution
            to_fill.append((i, j))
            return False

        backtrack()
