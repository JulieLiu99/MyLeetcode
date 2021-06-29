class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        """
        Time O(n)
        Space O(1): maybe plus a bit of recursion O(difference in length)
        
        """
        
        i = len(a) - 1
        j = len(b) - 1
        res = ""
        carry = 0
        
        # loop both strings together from end to front 
        # until shorter one is fully visited 
        while i >= 0 and j >= 0:
            # 0 + 0 = 0
            if a[i] == "0" and b[j] == "0":
                if carry == 0:
                    res = "0" + res
                else:
                    res = "1" + res
                    carry = 0
            # 1 + 0 = 1
            elif a[i] == "0" or b[j] == "0":
                if carry == 0:
                    res = "1" + res
                else:
                    res = "0" + res
            # 1 + 1 = 10
            else:
                if carry == 0:
                    res = "0" + res
                    carry = 1
                else:
                    res = "1" + res
            i -= 1
            j -= 1
                 
        # append the front of the longer str
        # call self.addBinary in case need to handle carry on from while loop
        if i >= 0:
            if carry == 0:
                res = a[:i+1] + res
            else:
                res = self.addBinary(a[:i+1], "1") + res
                carry = 0
        if j >= 0:
            if carry == 0:
                res = b[:j+1] + res
            else:
                res = self.addBinary(b[:j+1], "1") + res
                carry = 0
         
        # finally handle if carry on still exists
        # return result
        if carry == 0:
            return res
        else: 
            res = "1" + res
            return res
