class Solution:
    def calculate(self, s: str) -> int:
        """
        Stack + Recursion
        
        If (, start recursion with a new stack, and from next char onwards
        If ), return calculation and index
        
        Time O(n)
        Space O(n)
        
        E.g.    1+(2+3)+4$
                ^              -> stack = [], operator = +, num = 1
                1+(2+3)+4$
                 ^             -> stack = [1], operator = +, num = 0
                1+(2+3)+4$
                  ^^^^^        -> inner layer returns num = 5, i = 6
                1+(2+3)+4$
                       ^       -> stack = [1, 5], operator = +, num = 0
                1+(2+3)+4$
                        ^      -> stack = [1, 5], operator = +, num = 4
                1+(2+3)+4$
                         ^     -> stack = [1, 5, 4]
        result = 1 + 5 + 4 = 10
        """
        
        s = s +"$" # mark the end
        
        def calculator(stack, i):
            num = 0
            operator = "+" # append +num for the first num
            
            while i < len(s):
                char = s[i]
                if char == " ":
                    continue
                elif char.isdigit():
                    num = num * 10 + int(char)
                # If inner layer, evaluate it first
                elif char == "(":
                    num, i = calculator([], i+1)
                # If  +-*/), process current num
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
                    # end of recursion, return current calculation
                    if char == ")":
                        return sum(stack), i
                    operator = char # new operator
                    num = 0
                i += 1
                
            return sum(stack)
        
        return calculator([], 0)
