class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        DP
        
        could be top down recursion
        but more efficient bottom up DP table
        
        Time O(N^2)
        Space O(N^2)
        """
        # table[i][j]: the match status between p[:i] and s[:j]
        # table[0][0]: the match status of two empty strings
        # check p[i-1] and s[j-1] to update table[i][j]

        # Initialize the table with False
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        # Two empty strings always match
        table[0][0] = True

        # When s is an empty string but p is not, update if '*'
        for i in range(2, len(p) + 1):
            table[i][0] = table[i-2][0] and p[i-1] == '*'

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i-1] != "*":
                    table[i][j] = table[i-1][j-1] and \
                                  (p[i-1] == s[j-1] or p[i-1] == '.')
                else:   
                    # * eliminate the previous or count the previous
                    table[i][j] = table[i-2][j] or table[i-1][j]

                    # True if p's previous one is equal to the current s
                    if p[i-2] == s[j-1] or p[i-2] == '.':
                        table[i][j] |= table[i][j-1]

        return table[-1][-1]
