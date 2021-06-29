class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        i = len(digits) - 1
        
        if digits[i] != 9:
            digits[i] += 1
            
        else:
            digits[i] = 0
            # move to previous digit
            i -= 1
            # loop forward until digits[i] smaller than 9
            while i >= 0 and digits[i] == 9:
                digits[i] = 0
                i -= 1
            if i < 0:
                digits = [1] + digits
            else:
                digits[i] += 1
            
        return digits
