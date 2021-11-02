class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """
        Cells at same diagonal line have the same i+j !!!
        """
        diagonals = []
        for i, r in enumerate(nums):
            for j, val in enumerate(r):
                if len(diagonals) <= i + j: # first element at diagonal
                    diagonals.append([val])
                else:
                    diagonals[i+j].append(val)
        res = []
        for diagonal in diagonals:
            res += reversed(diagonal) # reverse because vals at first row are last elements of diagonal
        return res
                    
                    
