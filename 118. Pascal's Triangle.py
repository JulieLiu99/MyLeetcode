class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        """
        Apart from the first and final element 1,
        Each row is derived by summing up pairs of elements from the previous row.
        
        Time O(n): each element gets summed once or twice
        Space O(numRows): for tesmporary new_row[]
        
        """
        
        res = [[1]]     # initialize first row
        
        for n in range(1, numRows):   # size of previous row, from 1 to numRows-1
            
            new_row = [1]
            i = 0   
            while (i+1) < n:
                new_row.append(res[-1][i] + res[-1][i+1])
                i += 1
            new_row += [1]
            
            res += [new_row]    # [new_row] instead of new_row because we want it to be subarray inside res[]
            
        return res
