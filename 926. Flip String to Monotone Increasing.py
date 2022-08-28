class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        '''
        No need to flip when 1 is on the tail of current substring
        
        Need to flip when 0 is on the tail of current substring
            - option_1: flip current 0 to 1
            - option_2: flip all leading 1s to 0s
            
        Time: O(N)
        Space: O(1)
        '''
        
        count_1 = 0
        flip = 0
        
        for char in s:
            if char == '1':
                count_1 += 1
            else:
                # option_1: flip current 0 to 1
                # option_2: flip all leading 1s to 0s
                flip = min(flip + 1, count_1)
                
        return flip
