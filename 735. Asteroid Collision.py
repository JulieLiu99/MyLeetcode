class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        plus = []
        minus = []
        for a in asteroids:
            if a > 0: # a is plus
                plus.append(a)
            else:     # a is minus
                while plus and plus[-1] < abs(a):
                    plus.pop()
                if plus and plus[-1] == abs(a):
                    plus.pop()
                elif not plus:
                    minus.append(a)
                
        # if both remain, minus must be on the left side, plus must be on the right side
        return minus + plus
