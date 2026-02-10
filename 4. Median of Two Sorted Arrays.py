class Solution:
    def findMedianSortedArrays(self, A, B):
        """
        Binary search for splitting point in array A

        A: [ ... A_left | A_right ... ]
        B: [ ... B_left | B_right ... ]

        The left side contains exactly half of all elements
        We want to find a partition where everything on the left is ≤ everything on the right

        The median lies between the max of the left side and the min of the right side

        Time O(log(min(m, n)))
        Space O(1)
        """
        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        total_left = (m + n + 1) // 2 # median is in total_left if odd

        l, r = -1, m
        while l + 1 < r:
            cutA = l + (r - l) // 2
            cutB = total_left - cutA

            if A[cutA] < B[cutB - 1]: # A_right < B_left -> cutA too small
                l = cutA
            else:
                r = cutA

        cutA = r
        cutB = total_left - cutA

        # left side max
        A_left = A[cutA - 1] if cutA > 0 else float('-inf')
        B_left = B[cutB - 1] if cutB > 0 else float('-inf')
        left_max = max(A_left, B_left)

        if (m + n) % 2 == 1: return left_max # odd -> return left_max

        # right side min
        A_right = A[cutA] if cutA < m else float('inf')
        B_right = B[cutB] if cutB < n else float('inf')
        right_min = min(A_right, B_right)

        return (left_max + right_min) / 2.0 # even -> return average of left_max and right_min

