class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        Add digit by digit from back to front
        Keep track of carry
        
        Time O(n)
        Space O(1)
        
        """
        # make num2 the larger one
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        res = ""
        
        while i >= 0 and j >= 0:
            s = int(num1[i]) + int(num2[j]) + carry
            carry = s // 10
            digit = s % 10
            res = str(digit) + res
            i -= 1
            j -= 1
            
            
        # if one of the nums is larger, keep add it and the carry 
        while j >= 0:
            s = int(num2[j]) + carry
            carry = s // 10
            digit = s % 10
            res = str(digit) + res
            j -= 1
            
        # if carry in the end
        if carry:
            res = "1" + res
            
        return res
