class Solution:
    def calculate(self, s: str) -> int:
        """
        Stack
        
        Whenver we have an operater and a number
        If + or -: push num or -num into stack
        If * or /: pop previous num, do the calculation, and push result to stack
        
        Time O(n)
        Space O(n)
        
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
                
                if not operator: # the first num
                    stack.append(curNum)
                    
                elif operator == "+":
                    stack.append(curNum)
                    
                elif operator == "-":
                    stack.append(-curNum)
                    
                elif operator == "*":
                    prev = stack.pop()
                    stack.append(prev * curNum)
                    
                else:
                    prev = stack.pop()
                    if prev % curNum and prev/curNum < 0:
                        stack.append(prev//curNum + 1) # truncate toward zero
                    else:
                        stack.append(prev//curNum )
                
                operator = c # record new operator
                curNum = 0 # reinitiate for new number
                    
        return sum(stack)
