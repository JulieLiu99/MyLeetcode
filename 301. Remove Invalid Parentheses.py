class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        """
        BFS
        
        Let's model the problem as a graph,
        Node: all possible string by removing parenthesis (The start node is `s`).
        Edge (from u to v): by removing a parentheses of u.
        
        As a result, the problem becomes to get the shortest distance from s to a valid node (assuming at level l) in the first place; then get all valid nodes within level l.
        Shortest-path problem is natural to BFS.
        
        Time O(n2^n): validate (which takes N time) every combination of taking/not taking every parenthesis (which there are 2^N combinations).
        Space (2^n): storing all combinations in a level.
        
        """
#         # set is used here in order to avoid duplicate element
#         level = {s}
#         while True:
#             valid = []
#             for elem in level:
#                 if self.isValid(elem):
#                     valid.append(elem)
#             if valid:
#                 return valid

#             new_level = set()
#             # BFS
#             # {'()())()'}
#             # 0  )())()
#             # 1 ( ())()
#             # 2 () ))()
#             # 3 ()( )()
#             # 4 ()() ()
#             # 5 ()()) )
#             # 6 ()())( 
#             # {'()()()', '()))()', ')())()', '(())()', '()())(', '()()))'}
#             for elem in level:
#                 for i in range(len(elem)):
#                     new_level.add(elem[:i] + elem[i + 1:])
#             level = new_level
    
#     def isValid(self,s):
#         count = 0
#         for c in s:
#             if c == '(':
#                 count += 1
#             elif c == ')':
#                 count -= 1
#                 if count < 0:
#                     return False
#         return count == 0

        """
        Each char can either be or not be in the s
        Instead of checking if every string is valid
        Check if "(" is always >= ")", and if in the end they have same counts
        ^ Counts are updated while building all possible strings
        
        Time O(2^n):    but actualy slower... 
                        because this exhaust all possible string
                        whereas in the previous solution we stop as soon as we get valid ones
        Space O(2^n)
        
        """
    
#         self.max_len = 0
#         self.res = set()
#         n = len(s)
        
#         def dfs(temp, temp_len, i, l, r):
            
#             if i == n:  # visited every char in s
#                 if l == r:   
#                     if temp_len > self.max_len: # larger lenght, fewer removal
#                         self.res = {temp}
#                         self.max_len = temp_len
#                     elif temp_len == self.max_len:
#                         self.res.add(temp)
#                 return    
            
#             if r > l: return  # already invalid 
            
#             if s[i] == "(":
#                 dfs(temp+s[i], temp_len+1, i+1, l+1, r)     # to be
#                 dfs(temp, temp_len, i+1, l, r)              # or not to be
#             elif s[i] == ")":
#                 dfs(temp+s[i], temp_len+1, i+1, l, r+1)     # to be
#                 dfs(temp, temp_len, i+1, l, r)              # or not to be
#             else:                                   
#                 dfs(temp+s[i], temp_len+1, i+1, l, r)       # non-parenthesis, keep
                
#         dfs("", 0, 0, 0, 0)
        
#         return list(self.res)
                
    
        """
        Best Performance So Far
        AND My Own Solution Yayyy !!!
        
        Get a stack of invalid parenthese
        Each time we pop one invalid parenthsis, and try to find its position
        
        BFS
        Try deleting the popped invalid parenthesis at different positions within one string 
        All possible outcomes after deleting this parenthesis is stored 
        Stored outcomes from this level serve as starting strings for deleting next invalid parenthesis
        
        Checking
        In the end we have a set of unique strings, 
        Each with all invalid parenthese deleted at different positions, compared to initial s
        Check them and return the valid ones
        
        
        Optimization:
        
        1. compared to ^ dfs, we do not need to determine to be or not to be for every char in s
        -> we only need to find within s the pisitions of the invalid chars
        
        2. compared to previous bfs, we do not need to try deleting every single char within that level
        -> we only need to try deleting char if it is equal to the current invalid char
        
        Time O(2^n + n^2):  O(2^n) possible st 
                            and for the final level of st, filtering out the valid ones takes O(n^2)
        Space O(2^n)
        
        """   
        
        cur = set([s])
        new = set()
        stack = self.invalid(s)
        
        while stack:
            c = stack.pop()
            for st in cur:
                for i in range(len(st)):
                    if st[i] == c:
                        new.add(st[:i] + st[i+1:])
            cur = new
            new = set()
            
        res = []
        for st in cur:
            if self.isValid(st):
                res.append(st)
                
        return res
    
    def isValid(self,s):
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

    def invalid(self, s):
        stack = []
        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(c)
        return stack
            