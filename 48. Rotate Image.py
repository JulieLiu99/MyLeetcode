class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        Time O(n^2)
        Space O(1)
        
        """
        l, r = 0, len(matrix) - 1
        
        while l < r:
            # modify current layer/circle
            # i = 0, ..., r - l - 1 (r = l+1)
            for i in range(r - l):
                top, bottom = l, r
                
                # save the original top left value
                topLeft = matrix[top][l+i]
                
                # move bottom left into top left
                matrix[top][l+i] = matrix[bottom-i][l]
                
                # move bottom right into bottom left
                matrix[bottom-i][l] = matrix[bottom][r-i]
                
                # move top right into bottom right
                matrix[bottom][r-i] = matrix[top+i][r]
                
                # move top left into top right
                matrix[top+i][r] = topLeft

            # shrink into inner layer/circle
            l += 1
            r -= 1
