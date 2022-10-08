class Solution:
    def countOfAtoms(self, formula: str) -> str:
        """
        Stack: process inner layer first, similar to calculator
        
        K4(ON(SO3)2)2
        ^^ -> put into stack {K: 4}
        
        K4(ON(SO3)2)2
           ^^ -> put into stack {O: 1, N: 1}
           
        K4(ON(SO3)2)2
              ^^^ -> put into stack {S: 1, O: 3}
              
        K4(ON(SO3)2)2
                 ^^ -> pop from stack, multiply by 2 {S: 3, O: 6}, add to current top {S: 2, O:7, N: 1}
                 
        K4(ON(SO3)2)2
                   ^^ -> -> pop from stack, multiply by 2 {S: 4, O:14, N: 2}, add to current top {S: 4, O:14, N:2, K: 4}
                   
        Sort and contatenate
        
        Time O(n^2)
        Space O(n): size of stack bounded by length of string
        """
        n = len(formula)
        stack = [collections.Counter()]
        i = 0
        
        while i < n:
            c = formula[i]
            
            if c == "(":
                stack.append(collections.Counter())
                i += 1
                
            elif c == ")":
                cur_counter = stack.pop()
                # find the multiplier after ")"
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[start:i]) if formula[start:i] else 1
                
                # multiply inner layer
                for atom, count in cur_counter.items():
                    stack[-1][atom] += count * multiplier
                    
            else:
                # find atom: 1 * UPPER  + (0 or more) * lower
                atom = c
                i += 1
                start = i
                while i < n and formula[i].islower():
                    i += 1
                atom += formula[start: i]
                
                # find count
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i]) if formula[start:i] else 1
                
                stack[-1][atom] += count
        
        res = ""
        res_counter = stack[-1]
        for atom in sorted(res_counter):
            if res_counter[atom] == 1:
                res += atom
            else:
                res += atom + str(res_counter[atom])
                
        return res
                
