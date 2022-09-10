class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        
        m, n = len(board), len(board[0])
        
        while True:
            # 1. Check
            crush = set()
            for i in range(m):
                for j in range(n):
                    if j >= 2 and board[i][j] and board[i][j] == board[i][j-1] == board[i][j-2]: # verticle
                        crush |= {(i, j), (i, j-1), (i, j-2)}
                    if i >= 2 and board[i][j] and board[i][j] == board[i-1][j] == board[i-2][j]: # horizontal
                        crush |= {(i, j), (i-1, j), (i-2, j)}

            # 2. Crush
            if not crush: break
            for i, j in crush: 
                board[i][j] = 0

            # 3. Drop
            for col in range(n): # drop column by column
                bottom_row = row = m-1
                while row >= 0:
                    if board[row][col] == 0: 
                        row -= 1
                    else: # nonzero val -> swap with bottom 
                        board[bottom_row][col], board[row][col] = board[row][col], board[bottom_row][col]
                        bottom_row -= 1
                        row -= 1
        return board
