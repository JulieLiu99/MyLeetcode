class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        """
        DP

        nums = [1, 2, 1]
                ----
                    ----  answer is 3
        %2   = [1, 0, 1]
                ^     ^
        every other num has the same remainder -> subsequence length + 1

        (x1 + x2) % k = (x2 + x3) % k
        x1 % k = x3 % k

        Time O(nk)
        Space O(k^2)
        """
        # dp[a][b] = len of the longest subsequence, where
        # the last two numbers have remainders a, b
        dp = [[0] * k for _ in range(k)]
        max_length = 0

        for num in nums:
            cur_remainder = num % k

            # subsequence does not have to be continuous
            # check all possible prev nums
            for prev_remainder in range(k):
                # extend cur -> prev -> cur
                #                    ^^^^^^ len + 1
                dp[prev_remainder][cur_remainder] = dp[cur_remainder][prev_remainder] + 1

                # track the longest subsequence found so far
                max_length = max(max_length, dp[prev_remainder][cur_remainder])

        return max_length
