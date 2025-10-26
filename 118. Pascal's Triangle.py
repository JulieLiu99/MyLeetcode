class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        """
        Apart from the first and final element 1,
        Each element is sum of pairs of elements from the prev_row.
        
        Time O(n): each element gets summed once or twice
        Space O(numRows): for tesmporary prev_row & row
        
        """
        
        res = [[1]]  # first row

        for _ in range(1, numRows):
            prev_row = res[-1]
            row = [1]
            
            # each inner element = sum of two elements above it
            for i in range(1, len(prev_row)):
                row.append(prev_row[i - 1] + prev_row[i])
            
            row.append(1)
            res.append(row)
        
        return res

