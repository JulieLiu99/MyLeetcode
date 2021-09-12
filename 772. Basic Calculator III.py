class Solution:
    def calculate(self, s: str) -> int:
        """
        Stack
        
        If (, start recursion with a new stack, and from next char onwards
        If ), return calculation and index
        
        Time O(n)
        Space O(n)
        
        """
        
        s = s+"$"
        
        def calculator(stack=[], i=0):
            num = 0
            operator = "+"
            
            while i<len(s):
                c = s[i]
                if c == " ":
                    continue
                elif c.isdigit():
                    num = num * 10 + int(c)
                # If new expression, evaluate it first
                elif c == "(":
                    num, i = calculator([], i+1)
                else:
                    if operator == "+":
                        stack.append(num)
                    elif operator == "-":
                        stack.append(-num)
                    elif operator == "*":
                        stack[-1] *= num
                    elif operator == "/":
                        sign = 1 if stack[-1] * num >= 0 else -1
                        stack[-1] = abs(stack[-1])//abs(num) # truncate toward zero
                        stack[-1] *= sign
                    # end of recursion, put it at end of current calculation
                    if c == ")":
                        return sum(stack), i
                    num = 0
                    operator = c
                i += 1
                
            return sum(stack)
        
        return calculator()
