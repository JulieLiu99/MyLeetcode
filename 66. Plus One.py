class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        i = len(digits) - 1
        
        if digits[i] != 9:
            digits[i] += 1
            
        else:
            # make digits[i] = 0 if originally 9
            # move forward until digits[i] smaller than 9
            while i >= 0 and digits[i] == 9:
                digits[i] = 0
                i -= 1
            # no digit smaller than 9 to increment
            # add 1 at the begining, e.g. [9] -> [1, 0]
            if i < 0:
                digits = [1] + digits
            # add 1 to digits[i] that is smaller than 9 
            else:
                digits[i] += 1
            
        return digits