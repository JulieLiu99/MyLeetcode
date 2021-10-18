class Solution:
    def myAtoi(self, s: str) -> int:
        
        """
        Time O(N): one iteration over the string
        Space O(1): constant extra space for storing sign, length, and position
        
        """
        
        s = s.strip() # trim white space
        if not s: return 0
        
        MAX_NUM = 2 ** 31 - 1
        MIN_NUM = -2 ** 31
        
        if s[0] == '-':
            sign = -1
            i = 1
        elif s[0] == '+':
            sign = 1
            i = 1
        else:
            sign = 1
            i = 0
            
        num = 0
        while i < len(s) and s[i].isdigit():
            cur_digit = ord(s[i]) - ord('0')
            # check before adding current digit
            # 2^31 - 1 = 2147483647
            if num > MAX_NUM//10 or (num == MAX_NUM//10 and cur_digit > 7): 
                return MAX_NUM if sign == 1 else MIN_NUM
            num = num * 10 + cur_digit
            i += 1
        
        return sign * num  
