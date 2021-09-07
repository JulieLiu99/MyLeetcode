class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        From end to front
        Add two digits from a & b, and carry
        If sum = 10/11, carry = 1
        
        If one str comes to an end, 
        Only add digit from  the other string, and carry
        
        In the end, if there is carry, add last 1
        
        Time O(n)
        Space O(1)
        
        """
        
        res = ""
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        
        while i >= 0 and j >= 0:
            if int(a[i]) + int(b[j]) + carry == 0:
                res += "0"
                carry = 0
            elif int(a[i]) + int(b[j]) + carry == 1:
                res += "1"
                carry = 0
            elif int(a[i]) + int(b[j]) + carry == 2: # 10
                res += "0"
                carry = 1
            else: # 11
                res += "1"
                carry = 1
            i -= 1
            j -= 1

        while i >= 0:
            if int(a[i]) + carry == 0:
                res += "0"
                carry = 0
            elif int(a[i]) + carry == 1:
                res += "1"
                carry = 0
            else: # 10
                res += "0"
                carry = 1
            i -= 1
                
        while j >= 0:
            if int(b[j]) + carry == 0:
                res += "0"
                carry = 0
            elif int(b[j]) + carry == 1:
                res += "1"
                carry = 0
            else: # 10
                res += "0"
                carry = 1
            j -= 1
            
        if carry: res += "1"
        
                
        return res[::-1]
