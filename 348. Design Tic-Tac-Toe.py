class TicTacToe:
    
    def __init__(self, n: int):
        self.row = [0]*n
        self.col = [0]*n
        self.diag1 = 0
        self.diag2 = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        self.row[row] += 1 if player == 1 else -1
        self.col[col] += 1 if player == 1 else -1
        if row == col:
            self.diag1 += 1 if player == 1 else -1
        if col + row == self.n - 1:
            self.diag2 += 1 if player == 1 else -1
        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n or abs(self.diag1) == self.n or abs(self.diag2) == self.n: # current player has won
            return player
        return 0


