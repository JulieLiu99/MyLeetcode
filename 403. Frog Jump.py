class Solution:
    def canCross(self, stones: List[int]) -> bool:
        """
        DFS
        
        Time O(n^2)
        Space O(n^2)
        """
        memo = set() # to save the dead ends, for early termination
        target = stones[-1]
        stones = set(stones)
        
        def dfs(cur, speed, target):
            if (cur, speed) in memo:
                return False

            if cur == target:
                return True

            if cur > target or cur < 0 or speed <= 0 or cur not in stones:
                return False
            
            for next_speed in [speed-1, speed, speed+1]:
                if (cur + next_speed) in stones:
                    if dfs(cur + next_speed, next_speed, target):
                        return True

            memo.add((cur, speed))
            return False

        return dfs(1, 1, target)
