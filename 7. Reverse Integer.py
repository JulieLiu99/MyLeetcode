class Solution:
    def reverse(self, x: int) -> int:
        
        """
        Use string as an intermediate representation
        
        Time O(digit) 
        floor(log10(x)) + 1 is the number of digits in integer x
        Space O(1) no extra data structure
        """
        
        max_int = pow(2, 31)-1
        min_int = pow(-2, 31)

        negative = True if x < 0 else False
        
        str_x = str(abs(x))
        reversed_str_x = str_x[::-1]

        reversed_x = int(reversed_str_x)
        if reversed_x > max_int or reversed_x < min_int:
            return 0
        elif negative:
            return -1 * reversed_x
        else:
            return reversed_x
