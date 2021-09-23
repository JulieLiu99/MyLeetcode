class Solution:
    def encode(self, num: int) -> str:
        """
        1 digit has base 0, can hold 2^1 = 2 nums
        2 digits has base 3, can hold 2^2 = 4 nums
        3 digits has base 7, can hold 2^3 = 8 nums
        ...
        Length of encoded string is length, where 2^1 + 2^2 + .... + 2^length <= num 
        
        Then add how far num is from base "0" * length
        
        E.g. 6
        base = 0, length = 1, 6 > 1
        base = 3, length = 2, 6 > 3
        base = 7, length = 3, 6 < 7, reverse back to base = 3, length = 2
        
        base = "0" * length = 3
        6 - 3 = 3 in binary form = "11"
        No need to pad in the front anymore
         
        Time O(logn) = length of binaryString
        Space O(1)
        
        """
        if num == 0: return ''
        
        length = 1
        base = 1
        while num >= base:
            base += 2 ** length
            length += 1
          
        # at the final round, num < base already, reverse back
        length -= 1 
        base -= 2 ** length
        
        binaryString = bin(num - base)[2:]  # "0b11"
        
        if len(binaryString) == length:
            return binaryString
        else:
            prefix = '0' * (length - len(binaryString)) # padding in the front
            return prefix + binaryString
