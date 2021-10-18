class Solution:
    def numberToWords(self, num: int) -> str:
        """
        Recursion
        
        English expressions:
        0. Zero for num = 0
        1. 1 to 19 = One ~ Nineteen
        2. 20 to 99 = Twenty ~ Ninety + "" ~ Nine
        3. num//100 + Hundred + ...
           num//1,000 + Thousand + ...
           num//100,000 + Million + ...
           num//100,000,000 + Billion + ...
           
        For bigger nums, scales of 10^9, 10^6, 10^3 ... from big to small
        Handle head first (val is int division of this scale -> converted to "Name of val" + "Name of this scale")
        Then put tail (remainder after division of scale) into recursion
        
        Time O(n)
        Space O(n)
        
        """
        to19 = '- One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = '- - Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        
        # 1 billion = 10^9
        # 1 million = 10^6
        # 1 thousand = 10^3
        # 1 hundred = 10^2

        if num == 0: return "Zero"

        def recursor(num):
            
            if num == 0: 
                return ""
            
            # For 0 < nums <= 99:
            # if at start, one extra space -> handled at the end
            # if in middle, serve as space between this part and prev part -> any positive num will come here, so makes sense to add space here
            
            if num <= 19: 
                return " " + to19[num]    
            
            # 99 = tens[99//10] + to19[99%10] = Ninety Nine 
            # 20 = tens[20//10] = Twenty
            if num <= 99: 
                return " " + tens[num//10] + recursor(num%10) 
            
            # 100 = recursor(1) + " Hundred "+ recursor(0)
            # 101 = recursor(1) + " Hundred "+ recursor(1)
            # 999 = recursor(9) + " Hundred "+ recursor(99)
            if num <= 999: 
                return recursor(num//100) + " Hundred"+ recursor(num%100)
            
            # 1000 = recursor(1) + " Thousand "+ recursor(0)
            # 1001 = recursor(1) + " Thousand "+ recursor(1)
            # 9999 = recursor(9) + " Thousand "+ recursor(1)
            # max= 999 thousands + 9 hundred 99
            if num <= 10**6-1: 
                return recursor(num//1000) + " Thousand"+ recursor(num%1000)

            # max = 999 million + 999 thousand + 9 hundred 99
            if num <= 10**9-1: 
                return recursor(num//(10**6)) + " Million"+ recursor(num%(10**6))

            else: 
                return recursor(num//(10**9)) + " Billion"+ recursor(num%(10**9))

        return recursor(num)[1:]  # get rid of initial space
