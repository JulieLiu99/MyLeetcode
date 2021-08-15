class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        BFS
        
        From border to center mark all cells that don't need to be flipped
        Flipp the rest 'O''s
        
        Time O(N)
        Space O(border)
        
        """
        rows = len(board)
        cols = len(board[0])
        
        q = collections.deque()
        
        # push all cells on four borders to q
        for row in range(rows):
            q.append((row, 0))
            q.append((row, cols-1))

        for col in range(1, cols-1):
            q.append((0, col))
            q.append((rows-1, col))

        while q:
            row, col = q.popleft()
            if 0 <= row < rows and 0 <= col < cols and board[row][col] == 'O':
                board[row][col] = 'N'   # don't flip
                q.append((row-1, col))
                q.append((row+1, col))
                q.append((row, col+1))
                q.append((row, col-1))

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'N':
                    board[row][col] = 'O'
                else:
                    board[row][col] = 'X'

        """
        DFS
        
        From border to center mark all cells that don't need to be flipped
        Flipp the rest 'O''s
        
        Time O(N)
        Space O(N)
        
        """
#         def dfs(row, col):
#             if 0 <= row < rows and 0 <= col < cols and board[row][col] == 'O':
#                 board[row][col] = 'N'   # don't flip
#                 dfs(row+1, col)
#                 dfs(row-1, col)
#                 dfs(row, col+1)
#                 dfs(row, col-1)
            
#         rows = len(board)
#         cols = len(board[0])

#         # dfs from cells on four borders
#         for row in range(rows):
#             dfs(row, 0)
#             dfs(row, cols-1)
            
#         for col in range(1, cols-1):
#             dfs(0, col)   
#             dfs(rows-1, col)   
                
#         for row in range(rows):
#             for col in range(cols):
#                 if board[row][col] == 'N':
#                     board[row][col] = 'O'
#                 else:
#                     board[row][col] = 'X'
