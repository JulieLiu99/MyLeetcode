class Solution:
    def calculate(self, s: str) -> int:
        """
        Stack
        
        Whenver we have an operater and a number
        If + or -: push num or -num into stack
        If * or /: calculate with top of stack num
        
        Time O(n)
        Space O(n)
        
        Optimization: No need of stack. Keep track of total and last number.
        """
        stack = []
        s += "#" # ending mark, so that last operator & curNum can be processed
        operator = ""
        curNum = 0
        
        for i, c in enumerate(s):
            
            if c.isdigit():
                curNum = curNum*10 + int(c)
                
            # process previous operator and previous num
            elif c in "+-*/#":
                
                if not operator: # curNum is the first num
                    stack.append(curNum)
                    
                elif operator == "+":
                    stack.append(curNum)
                    
                elif operator == "-":
                    stack.append(-curNum)
                    
                elif operator == "*":
                    stack[-1] *= curNum
                    
                else: # '/'
                    stack[-1] = int(stack[-1] / curNum)  # truncate toward zero
                
                operator = c # record new operator
                curNum = 0 # reinitialize for new number
                    
        return sum(stack)
        
