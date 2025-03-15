class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """
        Two pointers scanning through two lists
        Merge intervals for each pair
        Time O(m+n)
        Space O(m+n)
        """
        intersections = []
        i = j = 0

        while i < len(A) and j < len(B):
            # Check if A[i] intersects B[j]
            start = max(A[i][0], B[j][0])
            end = min(A[i][1], B[j][1])
            if start <= end:
                intersections.append([start, end])

            # Remove the interval with the smallest endpoint
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return intersections
