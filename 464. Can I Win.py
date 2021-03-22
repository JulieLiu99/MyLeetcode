class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        """
        https://www.youtube.com/watch?v=GNZIAbf0gT0
        
        Time O(n*2^k): n = desiredTotal and k = maxChoosableInteger. 
        Worst case try every single combinatoin of k on each possible remainder.
        
        Space O(2^k): seen{}
        
        """
        seen = {}

        def can_win(choices, remainder):
            # if the largest choice exceeds the remainder, then we can win!
            if choices[-1] >= remainder:
                return True

            seen_key = tuple(choices)
            if seen_key in seen:    # make permuatation combination
                return seen[seen_key]

            # we haven't won yet.. it's the next player's turn
            # loop in reverse -> hit the winner case more quickly
            for index in reversed(range(len(choices))):
                if not can_win(choices[:index] + choices[index+1:], remainder - choices[index]):
                    seen[seen_key] = True
                    return True
                
            # we fail
            seen[seen_key] = False
            return False

        
        summed_choices = (maxChoosableInteger + 1) * maxChoosableInteger / 2
        if summed_choices < desiredTotal:
            return False
        if summed_choices == desiredTotal:
            return maxChoosableInteger % 2      # we win if odd number of turns

        choices = list(range(1, maxChoosableInteger + 1))
        
        return can_win(choices, desiredTotal)
