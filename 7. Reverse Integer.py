class Solution:
    def reverse(self, x: int) -> int:
        
        """
        :type x: int
        :rtype: int
        
        Time O(log(x)) 
        floor(log10(x)) + 1 is the number of digits in integer x
        Space O(1) no extra data structure
        """
        
        # res, sign = 0, 1
        # if x < 0:
        #     sign = -1
        #     x = -1 * x
        # while x != 0:
        #     pop = x % 10            # pop last digit
        #     x = int(x/10)           # retain the rest
        #     res = res * 10 + pop    # append the popped digit to end
        #     if (res > 2 ** 31 - 1) or (res > 2 ** 31 and sign == -1):
        #         return 0
        # return res * sign
        
        negative = False
        
        if x < 0: 
            negative = True
            x = str(x)[1:] # get rid of '-'
        else:
            x = str(x)
            
        # get rid of ending 0's
        end = len(x) - 1
        while end >= 0 and x[end] == "0":
            end -= 1
        
        # copy string from end to 0
        res = ""
        while end >= 0:
            res += x[end]
            end -= 1
            
        if not res: return 0 # res = '' for 0
        
        res = int(res)
        if res > 2 ** 31 - 1 or (res == 2 ** 31 - 1 and negative):
            return 0
        if negative: 
            return -1 * res
        else:
            return res