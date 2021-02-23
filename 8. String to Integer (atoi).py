class Solution:
    def myAtoi(self, s: str) -> int:
        
        """
        Time O(N): one iteration over the string
        Space O(1): constant extra space for storing sign, length, and position
        
        """
        
        sign = 1
        max_int, min_int = 2147483647, -2147483648
        
        result, pos = 0, 0
        ls = len(s)
        while pos < ls and s[pos] == ' ':     # leading whitespace
            pos += 1
        if pos < ls and s[pos] == '-':        # sign
            sign = -1
            pos += 1
        elif pos < ls and s[pos] == '+':
            pos += 1
            
        while pos < ls and ord(s[pos]) >= ord('0') and ord(s[pos]) <= ord('9'):
            # ord() function returns an integer representing the Unicode character
            
            num = ord(s[pos]) - ord('0')
            
            if result > int(max_int/10) or ( result == int(max_int/10) and num >= 8):
                if sign == -1:
                    print(min_int)
                    return min_int
                return max_int
            result = result * 10 + num
            
            pos += 1
                        
        return sign * result
