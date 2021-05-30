class Solution:
    """
    Recursion
    
    (Base) Case 1: if there is 0 symbol, 
	we simply add input to result list;
    
    Case 2: if there is 1 symbol, 
	e.g., 1 s 2, we calculate the input and the result add to result list;
    
    Case 3: if there are 2 symbols, 
	e.g., 1 s 2 s 3, we can add parentheses when we meet a symbol as below:
	1 s (2 s 3) and (1 s 2) s 3.
	In this way, 1, (2 s 3), (1 s 2), and 3 can all be solved based on the above base cases, and we combine the result accoringly and add to result list.
    
    Time O(2^n) 
    """
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        memo = {}
        if expression.isdigit():
            return [int(expression)]
        if expression in memo:
            return memo[expression] 
        
        res = []
        for i in range(len(expression)):
            # operator --> split here and calculate
            if expression[i] in "-+*":
                res1 = self.diffWaysToCompute(expression[:i])
                res2 = self.diffWaysToCompute(expression[i+1:])
                for x in res1:
                    for y in res2:
                        res.append(self.calculate(x, y, expression[i]))
        memo[expression] = res
        return res

    def calculate(self, x, y, op):
        if op == "+":
            return x+y
        elif op == "-":
            return x-y
        else:
            return x*y
