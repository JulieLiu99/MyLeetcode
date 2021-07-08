"""
DFS Recursion

Time O(width*height*4^len(word))
where k is length of word and m and n are sizes of our board
Start from all possible cells of board O(width*height)
at each cell/char we can go in 4 directions
Each dfs search is O(4^len(word)) because won't stop until the end of the word or deadend 
In practice however this number will be usually much smaller, because of a lot of dead-ends. 

Space O(len(word)) - potential size of recursion stack. 

"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n = len(word)
        height = len(board)
        width = len(board[0])
        
        def dfs(board, row, col, i):
            # i is always the next char, so till n
            if i ==  n: return True

            # out of bound
            if row<0 or row>=height or col<0 or col>=width: return False

            # not matched or taken
            if board[row][col] != word[i]: return False

            tmp = board[row][col]  
            board[row][col] = -1    # mark as visited

            res = dfs(board, row+1, col, i+1) or dfs(board, row-1, col, i+1) or dfs(board, row, col+1, i+1) or dfs(board, row, col-1, i+1)

            # revert cell back before return!!!!!!!!!!!!!!!
            # so we have correct board to start next search
            board[row][col] = tmp   

            return res
    
    
        for row in range(height):
            for col in range(width):
                # check whether can find word, starting at (row, col) position 
                if dfs(board, row, col, 0):
                    return True
                
        return False
