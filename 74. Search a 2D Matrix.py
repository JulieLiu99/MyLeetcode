class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Binary search
        
        Think of it as searching for target in a flat array
        convert index in flat array to index in matrix
        matrix[idx//width][idx%width]
        
        Time O(logmn)
        Space O(1)
        
        """
        
        height = len(matrix)
        width = len(matrix[0])
        if height == 0 or width == 0: return False
        
        l = -1
        r = width*height
        
        while l + 1 != r:
            mid = l + (r-l)//2
            cur = matrix[mid//width][mid%width]
            if cur == target:
                return True
            elif cur < target:
                l += 1
            else:
                r -= 1
            
        return False
