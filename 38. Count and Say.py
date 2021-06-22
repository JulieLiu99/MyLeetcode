class Solution:
    def countAndSay(self, n: int) -> str:
        
        """
        Recursive
        
        """
        if n == 1: return "1"
        
        s = self.countAndSay(n-1)
        
        i, char, tmp = 0, s[0], ''
        
        for j in range(1, len(s)):
            # end of a contiguous section 
            if s[j] != char:
                tmp += str(j-i) + char
                i = j
                char = s[j]
        # last contiguous section 
        tmp += str(len(s)-i) + char
        
        return tmp
    

        """
        Iterative
        
        """
        # initilize result for countAndSay(1) = "1" 
        result = '1'
        
        # already took care of first char
        for _ in range(n-1):
            s = result
            result = ''
            j = 0
            # start of a unique char
            while j < len(s):
                char = s[j]
                count = 1
                j += 1
                # a contiguous section 
                while j < len(s) and s[j] == char:
                    count += 1
                    j += 1
                result += str(count) + str(char)
                
        return result
