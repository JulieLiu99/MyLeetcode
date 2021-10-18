class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        
        follow = 0
        
        for x in data:
            
            if follow: # 10xxxxxx * (n - 1 bytes)
                if int('10000000', 2) <= x <= int('10111111', 2): 
                    follow -= 1
                else: 
                    return False
                
            else: # first byte
                if x >= int('11111000', 2): # too big
                    return False
                if x >= int('11110000', 2): # 11110xxx
                    follow = 3
                elif x >= int('11100000', 2): # 1110xxxx
                    follow = 2
                elif x >= int('11000000', 2): # 110xxxxx
                    follow = 1
                elif x >= int('10000000', 2) or x < 0: # 0xxxxxxx
                    return False
                
        return follow == 0
