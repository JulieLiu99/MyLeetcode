class Solution:
    def intToRoman(self, num: int) -> str:
        """
        both time and space are O(1)
        """
        
        symbols = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'} 
        
        roman = ""
        
        for value in symbols.keys():
            
            # convert to currently largest symbol if possible
            roman += (num//value) * symbols[value]
            
            # get remainder
            num %= value
        
        return roman
