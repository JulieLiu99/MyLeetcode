class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        36 * 23
        = (6*3 + 6*20) + (30*3 + 30*20)
        """
        res = 0
        carry1 = 1 
        
        for i in num1[::-1]: 
            carry2 = 1 
            for j in num2[::-1]:  
                res += int(i) * int(j) * carry1 * carry2
                carry2 *= 10 # after first iteration (number 6 is covered), it goes to the next number from right, which is 3 here, actually 30, right? That's why it multiplies the carry2 by 10. Similar for carry1. 
            carry1 *= 10
        return str(res)
