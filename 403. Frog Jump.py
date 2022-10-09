class Solution:
    def canCross(self, stones: List[int]) -> bool:
        """
        DFS
        
        Time O(n^2)
        Space O(n^2)
        """
        memo = set() # to save the dead ends, for early termination
        start = stones[0]
        target = stones[-1]
        stones = set(stones)
        
        def dfs(cur, speed, target):
            if (cur, speed) in memo:
                return False

            if cur == target:
                return True

            if cur > target or cur < 0 or speed <= 0:
                return False
            
            for next_speed in [speed-1, speed, speed+1]:
                if (cur + next_speed) in stones:
                    if dfs(cur + next_speed, next_speed, target): # jump to next
                        return True

            memo.add((cur, speed))
            return False
        
        if start + 1 not in stones: # assume the first jump must be 1 unit
            return False
        return dfs(start + 1, 1, target)
