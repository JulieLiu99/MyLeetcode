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
        # set is used here in order to avoid duplicate element
        level = {s}
        while True:
            print(level)
            valid = []
            for elem in level:
                if self.isValid(elem):
                    valid.append(elem)
            if valid:
                return valid

            new_level = set()
            # BFS
            # {'()())()'}
            # 0  )())()
            # 1 ( ())()
            # 2 () ))()
            # 3 ()( )()
            # 4 ()() ()
            # 5 ()()) )
            # 6 ()())( 
            # {'()()()', '()))()', ')())()', '(())()', '()())(', '()()))'}
            for elem in level:
                for i in range(len(elem)):
                    print(i, elem[:i], elem[i + 1:] )
                    new_level.add(elem[:i] + elem[i + 1:])
            level = new_level
    
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
