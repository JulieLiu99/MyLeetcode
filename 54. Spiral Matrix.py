class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        """
        Append layer by layer
        
        i for layer/circlr
        t, b, l, r for vertices in each layer/circle
        
        Time O(n)
        Space O(1)
        
        """
        
        t = 0
        b = len(matrix) - 1
        l = 0
        r = len(matrix[0]) - 1
        
        size = len(matrix) * len(matrix[0])
        res = []
        i = 0   # layer/circle
        
        while t<b or l<r:
            # checking len(res) < size before appending anything because
            # otherwise [[6,9,7]] has
            # right [6, 9]
            # down [6, 9]
            # left [6, 9, 7, 9] -> one duplicate 9
            
            # go right
            while l < r and len(res) < size:
                res.append(matrix[t][l])
                l += 1
            l = 0 + i
            # go down
            while t < b and len(res) < size:
                res.append(matrix[t][r])
                t += 1
            t = 0 + i
            # go left
            while l < r and len(res) < size:
                res.append(matrix[b][r])
                r -= 1
            r = len(matrix[0]) - 1 - i
            # go up
            while t < b and len(res) < size:
                res.append(matrix[b][l])
                b -= 1
            b = len(matrix) - 1 - i

            # shrink
            i += 1
            t = 0 + i
            b = len(matrix) - 1 - i
            l = 0 + i
            r = len(matrix[0]) - 1 - i
        
        # append center one if needed
        if len(res) < size:
            res.append(matrix[t][l])
            
        return res
