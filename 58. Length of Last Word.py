class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        count = 0
        
        # get rid of space at back, e.g. "a "
        i = len(s)-1
        while s[i] == ' ' and i >= 0:
            i -= 1
        # i is last non empty char
        s = s[:i+1]
        
        # loop backward
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                break
            else:
                count += 1
                
        return count
