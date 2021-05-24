class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        """
        1. Recursion
        
        Case 0: score of () = 1
        Case 1: score of (A) = 2 * score of A
        Case 2: score of (A)(B)(C) = score of (A) + score of (B)(C)
        
        Time O(n) ~ O(n^2)
             Best case   ()()()...
             Worst case  (((...)))
        Space O(n)
                
        
        """
        
#         def score(s, l, r):
#             if r - l == 1:
#                 return 1
#             count=0
#             for i in range(l, r):
#                 if s[i] == '(':
#                     count += 1
#                 else:    # ')'
#                     count -= 1
#                 if count == 0:
#                     return score(s, l ,i) + score(s, i+1, r)
#             return 2 * score(s, l+1, r-1)
        
#         return score(s, 0, len(s)-1)   
    
    
        """
        2. Counting
        
        Scan the string left to righ, record number of open ( as d.
        When see (), add 2^(d-1) to score
        
        (()(())) --> (()) + ((())) = 2^1 + 2^2 = 6
        (()) has d = 2
        ((())) has d = 3
        
        (()(()())) --> (()) + ((())) + ((()))
        
        Time O(N) 
        Space O(1)
        
        """
        score = 0
        d = -1
        for i, c in enumerate(s):
            if c == "(":
                d += 1
            else:
                d -= 1
            if s[i:i+2] == "()":
                score += 1 << d
        return score


