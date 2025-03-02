class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Update boundary indexes while traversing by layer
        
        Time O(n)
        Space O(1)
        """
        if not matrix:
            return []

        result = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse from left to right along the top boundary
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # Traverse from top to bottom along the right boundary
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Check again because boundaries have changed
            if top <= bottom and left <= right:

                # Traverse from right to left along the bottom boundary
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

                # Traverse from bottom to top along the left boundary
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result

