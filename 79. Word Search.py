class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        """
        DFS
        
        use a visited set - TLE
        mark visited in place - can pass
        
        Time O(rows*cols * word_length): dfs from every cell
        Space O(word_length)
        
        """
#         rows = len(board)
#         cols = len(board[0])
#         visited = set()
        
#         def dfs(i, j, k):
            
#             if k == len(word): # all matched
#                 return True
            
#             if not (0 <= i < rows and 0 <= j < cols) or board[i][j] != word[k]: # check current
#                 return False
            
#             for (new_i, new_j) in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
#                 if (new_i, new_j) not in visited:
#                     visited.add((new_i, new_j))
#                     if dfs(new_i, new_j, k+1): 
#                         return True
#                     visited.remove((new_i, new_j))
#             return False
        
#         for i in range(rows):
#             for j in range(cols):
#                 if board[i][j] == word[0] and (i, j) not in visited: # start of search
#                     visited.add((i, j))
#                     if dfs(i, j, 0):
#                         return True
#                     visited.remove((i, j))
                
#         return False


        rows = len(board)
        cols = len(board[0])
        
        def dfs(i, j, k):
            
            if k == len(word): # all matched
                return True
            
            if not (0 <= i < rows and 0 <= j < cols) or board[i][j] != word[k]: # check current
                return False
            
            char = board[i][j]
            board[i][j] = "#"  # mark as visited
            
            for (new_i, new_j) in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if dfs(new_i, new_j, k+1): 
                    return True
            
            board[i][j] = char # revert to unvisited
            return False
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]: # start of search
                    if dfs(i, j, 0):
                        return True
                
        return False
