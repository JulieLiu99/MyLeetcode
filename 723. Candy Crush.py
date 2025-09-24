class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        """
        Three steps: 
            1. Check repeating values and save cells that should be crushed
            2. Crush them by marking 0s
            3. Drop column by column, by copying non zero values from bottom up

        No direct marking 0s in place because there can be more than 3 repeating cells

        Time O(m n)
        Space O(m n)
        """
        
        # m, n = len(board), len(board[0])
        
        # while True:
        #     # 1. Check
        #     crush = set()
        #     for i in range(m):
        #         for j in range(n):
        #             if j >= 2 and board[i][j] and board[i][j] == board[i][j-1] == board[i][j-2]: # verticle
        #                 crush |= {(i, j), (i, j-1), (i, j-2)}
        #             if i >= 2 and board[i][j] and board[i][j] == board[i-1][j] == board[i-2][j]: # horizontal
        #                 crush |= {(i, j), (i-1, j), (i-2, j)}

        #     # 2. Crush
        #     if not crush: break
        #     for i, j in crush: 
        #         board[i][j] = 0

        #     # 3. Drop
        #     for col in range(n): # drop by column from bottom up
        #         next_row = m - 1
        #         for row in range(m - 1, -1, -1):
        #             if board[row][col] > 0: # keep non-crushed cells
        #                 board[next_row][col] = board[row][col]
        #                 next_row -= 1
        #         for row in range(next_row, -1, -1): # fill the rest with zeros
        #             board[row][col] = 0
        # return board

        """
        Two steps:

        1. Mark all cells that should be crushed
           As negative instead of 0s (assumption: original values >= 0)
           So that we can detect more than 3 repeating cells

        2. Drop column by column, by copying positive values from bottom up

        Time O(m n)
        Space O(1)
        """
        
        m, n = len(board), len(board[0])

        while True:
            crushed = False

            # 1. Mark in place: negate any horizontal or vertical run ≥ 3
            for i in range(m):
                for j in range(n):
                    if board[i][j] == 0: # empty cell
                        continue
                    value = abs(board[i][j])
                    # horizontal check (left side)
                    if j >= 2 and value == abs(board[i][j-1]) == abs(board[i][j-2]):
                        crushed = True
                        board[i][j] = board[i][j-1] = board[i][j-2] = -value
                    # vertical check (top side)
                    if i >= 2 and value == abs(board[i-1][j]) == abs(board[i-2][j]):
                        crushed = True
                        board[i][j] = board[i-1][j] = board[i-2][j] = -value

            if not crushed:
                break

            # 2. Drop: compress positives downward; fill remainder with zeros
            for col in range(n):
                next_row = m - 1
                for row in range(m - 1, -1, -1):
                    if board[row][col] > 0: # only keep positive
                        board[next_row][col] = board[row][col]
                        next_row -= 1
                for row in range(next_row, -1, -1):
                    board[row][col] = 0

        return board
