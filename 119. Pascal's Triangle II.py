class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        Calculate numbers row by row.
        Each row is built upon the previous one,
        By adding all pairs of numbers
        
        Time O(n^2)
        Space O(n)
        
        """
        
        res = [1]
        
        if rowIndex == 0: return res
        
        for i in range(rowIndex):
            temp = [1]
            for j in range(len(res)-1):
                temp.append(res[j] + res[j+1])
            res = temp + [1]
            
            
        return res 
