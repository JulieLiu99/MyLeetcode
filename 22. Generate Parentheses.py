class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Backtracking
        
        Time O(2^(2n)) is exponential
        Runtime of backtracking algorithms is O(b^d), where b is the branching factor/base and d is the maximum depth of recursion.
        
        Space O(2^(2n)) + O(n) to store sequence
        """
        ans = []
        
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans
