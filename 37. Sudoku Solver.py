class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        DFS + backtracking

        Fill empties in order and try digits 1–9 using row/col/box checks
        
        Time O(9^n): for each cell try 9 different options
        Space O(n)
        
        """
        rows = [[False] * 9 for _ in range(9)]   # row constraints
        cols = [[False] * 9 for _ in range(9)]   # col constraints
        boxes = [[False] * 9 for _ in range(9)]  # box constraints

        empties = []  # list of (r, c) positions that need to be filled

        # map cell (r,c) to box index 0..8
        def box_id(r: int, c: int) -> int:
            return (r // 3) * 3 + (c // 3)

        # Step 1: initialize constraint tables from the given board
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    # record empty cell
                    empties.append((r, c))
                else:
                    # digit already present on board
                    d = int(board[r][c]) - 1        # '1'..'9' -> 0..8
                    b = box_id(r, c)                # which 3x3 box
                    rows[r][d] = True               # mark used in row
                    cols[c][d] = True               # mark used in col
                    boxes[b][d] = True              # mark used in box

        # Step 2: DFS over empties in fixed order
        def dfs(i: int, path: List[tuple]) -> bool:
            # base case: all empties filled -> solved
            if i == len(empties):
                return True

            # current empty cell
            r, c = empties[i]
            b = box_id(r, c)

            # try placing digits 1..9
            for d in range(9):
                # if digit already used in row/col/box -> cannot place
                if rows[r][d] or cols[c][d] or boxes[b][d]:
                    continue

                # ---- place digit ----
                board[r][c] = str(d + 1)            # write to board
                rows[r][d] = True                   # mark used in row
                cols[c][d] = True                   # mark used in col
                boxes[b][d] = True                  # mark used in box
                path.append((r, c))                 # path grows forward

                # recurse to next empty cell
                if dfs(i + 1, path):
                    return True                     # solution found

                # ---- backtrack (undo) ----
                path.pop()                          # remove from path
                board[r][c] = '.'                   # restore empty
                rows[r][d] = False                  # unmark row usage
                cols[c][d] = False                  # unmark col usage
                boxes[b][d] = False                 # unmark box usage

            # no digit works here -> dead end
            return False

        dfs(0, [])
