from typing import List

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        """
        For each right endpoint `r`:
        - start_limit is the largest index `a` such that there exists a conflicting pair (a, b) with b <= r
        - Therefore, valid subarrays ending at `r` start in (start_limit + 1) .. r

        Example:
        conflicts = [(2, 4), (3, 5)]

        At r = 4: (2, 4) forbids starts <= 2
        => start_limit = 2
        => valid subarrays ending at 4 start at 3

        At r = 5: (3, 5) forbids starts <= 3
        => start_limit = 3
        => valid subarrays ending at 5 start at 4

        => prev_start_limit = 2
        => if (3, 5) is removed, valid subarrays ending at 5 start at 3

        Time:  O(n + m)
        Space: O(n + m)
        """

        # register conflicts by the ending value b, because
        # the earliest time a conflict matters is when subarray’s right end reaches b
        conflicts_end_at = [[] for _ in range(n + 1)]
        for a, b in conflictingPairs:
            if a > b:
                a, b = b, a
            conflicts_end_at[b].append(a)

        valid_count = 0
        start_limit = 0 # largest `a` seen so far
        prev_start_limit = 0 # second largest `a` seen so far
        gain = [0] * (n + 1)

        # for each endpoint r, count valid subarrays (start_limit + 1) .. r
        for r in range(1, n + 1):
            # each conflict (a, r) means subarrays ending at r cannot start <= a
            for a in conflicts_end_at[r]:
                if a > start_limit:
                    prev_start_limit = start_limit
                    start_limit = a
                elif a > prev_start_limit:
                    prev_start_limit = a

            valid_count += r - start_limit

            # if conflict with start_limit is removed, allowed start moves back
            if start_limit > 0:
                gain[start_limit] += start_limit - prev_start_limit

        return valid_count + max(gain)
