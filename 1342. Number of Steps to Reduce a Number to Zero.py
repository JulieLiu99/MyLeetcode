class Solution:
    def numberOfSteps(self, num: int) -> int:
        """
        14 = 8 + 4 + 2 = 1110   move right 
                ->   7 =  111   change last bit + move right
                ->   6 =  110   
                ->   3 =   11   change last bit + move right
                ->   2 =   10
                ->   1 =    1   
                ->   0 =    0   + 1
        
        Time: O(bits of num)
        Space: O(1)
        
        """
        if num == 0: return 0
        
        steps = 0
        
        while num != 1:
            if num & 1: # odd: change last bit + move right
                steps += 2
            else:       # even: move right
                steps += 1
            num >>= 1
            
        return steps + 1  # we always need to move from 1 to zero
