class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        """
        BFS
        Swap 0 with its neighbors
        
        For every position of 0, moves has its possible swaps
        
        Time O(5!)
        Space O(5!)
        
        """
        moves = {0: {1, 3}, 1:{0, 2, 4}, 2:{1, 5}, 3:{0, 4}, 4:{1, 3, 5}, 5:{2, 4}}
        used = set()
        step = 0
        s = "".join(str(c) for row in board for c in row) # convert board to string, for better storage
        
        q = deque([(s, s.index("0"), 0)]) # (board, 0_position, step)
        while q:
            (s, i, step) = q.popleft()
            used.add(s)
            if s == "123450": # goal
                return step
            arr = [c for c in s]
            for move in moves[i]: # possible swap
                new_arr = arr[:]
                new_arr[i], new_arr[move] = new_arr[move], new_arr[i]
                new_s = "".join(new_arr)
                if new_s not in used:
                    q.append((new_s, move, step+1))
    
        return -1
