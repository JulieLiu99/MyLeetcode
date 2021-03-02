class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        # corner case: one row, or one vertical line only
        if numRows == 1 or numRows > len(s):  
            return s
        
        res = [''] * numRows  # a string for each line ['', '', '']
        row, step = 0, 0  
        
        for c in s:
            res[row] += c
            if row == 0:  # first row
                step = 1  # down
            if row == numRows - 1:  # last row
                step = -1  # up
            row += step # so that next c is added to another row
            
        return "".join(res)
