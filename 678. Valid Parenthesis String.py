class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # Counting
        # Go through s from both ends.
        # (1)Treat * as left parenthesis (, make sure ( always more than or equal to ).
        # (2)Treat * as right parenthesis ), make sure ) always more than or equal to (. 
        # l_count(1) and r_count(2) check the balance of parenthese. 
        # They can be larger than zero bc * can be empty, but not less than zero.
        # If there are enough ('s and )'s', return True.
        # Time O(n)
        # Space O(1)
        
        n = len(s)
        l_count = r_count = 0
        
        for i in range(n):
            l_count += 1 if s[i] in '(*' else - 1
            if l_count < 0: return False
            
        for i in range(n-1, -1, -1):
            r_count += 1 if s[i] in ')*' else -1
            if r_count < 0:
                return False
            
        return True