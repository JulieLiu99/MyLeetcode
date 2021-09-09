class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        """
        Backtracking DFS
        
        At each point, for next operand of length 1...n-i-1, could be "+ - *" in between
        Tricky case is "*", has to first delete the previously added operand
        
        Time O(4^n): between each digit, can be "nothing + - *"
        Space O(4^n)
        
        """
        
        res = []
        n = len(num)
        
        def dfs(i, path, val, last_addition):
            if i == n:             # end of traversal and successful
                if val == target:
                    res.append(path)
                else:
                    return
            else:
                for j in range(i, n):
                    # try [i..j] as an operand
                    if num[i] == '0' and j != i:
                        # For example "0555", Only consider "0" as possible operand
                        break
                    s = num[i : j + 1]
                    v = int(s)
                    if i == 0:
                        # no possible left operand
                        dfs(j + 1, s, v, v)
                    else:
                        dfs(j + 1, path + '+' + s, val + v, v)
                        dfs(j + 1, path + '-' + s, val - v, -v)
                        dfs(j + 1, path + '*' + s, val - last_addition + last_addition * v, last_addition * v)
        
        dfs(0, '', 0, 0)
        return res
