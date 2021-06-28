class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        size = n*n
        
        # matrix = [[-1]*n]*n
        # cannot initiate like this because
        # matrix[0][0] = 1 leads to 
        # [[1, -1, -1], [1, -1, -1], [1, -1, -1]]
        
        matrix = [[0 for _ in range(n)] for x in range(n)]
        
        t = 0
        b = n - 1
        l = 0
        r = n - 1
        
        x = 1   # value in cell
        i = 0   # layer/circle
        
        while t<b or l<r:
            # go left
            while l<r:
                matrix[t][l] = x
                x += 1
                l += 1
            l = 0 + i
            # go down
            while t<b:
                matrix[t][r] = x
                x += 1
                t += 1
            t = 0 + i
            # go left
            while l<r:
                matrix[b][r] = x
                x += 1
                r -= 1
            r = n - 1 - i
            # go up
            while t<b:
                matrix[b][l] = x
                x += 1
                b -= 1
            b = n - 1 - i
            
            # shrink
            i += 1
            t = 0 + i
            b = n - 1 - i
            l = 0 + i
            r = n - 1 -i
            
        # last center x not put in yet
        if x == size:
            matrix[t][l] = x
            
        return matrix
