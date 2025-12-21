
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        """
        DP
                     a a a b b c
                ->    aaa  bb  c
        group size     3   2   1
        combinations = 3 x 2 x 1 = 6 (to keep at least one per group)

        Time O(n + g*k)
        Space O(max(groups, k))
        """
        if not word:
            return 0

        MOD = 10**9 + 7
        groups = []
        count = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count) 

        total = 1
        for count in groups:
            total = (total * count) % MOD

        if k <= len(groups):
            return total

        # track invalid ways of selecting such that total pick is [0, k-1] < k
        # dp[s] = num of ways to select exactly s chars
        dp = [0] * k
        dp[0] = 1

        # sliding window sums valid ways to pick [1, count] chars from each group
        for count in groups:
            new_dp = [0] * k
            ways_to_select = 0

            for s in range(k):
                # to end with s total characters after this group, one must have had:
                # s-1 characters before (pick 1 here), or
                # s-2 characters before (pick 2 here),
                # …
                # s-count characters before.
                # new_dp[s] = dp[s-1] + dp[s-2] + ... + dp[s-count]
                if s > 0:
                    ways_to_select = (ways_to_select + dp[s - 1]) % MOD # add new term
                if s > count:
                    ways_to_select = (ways_to_select - dp[s - count - 1]) % MOD # remove old term
                new_dp[s] = ways_to_select

            dp = new_dp

        invalid = sum(dp) % MOD
        # numbers have been taken modulo so + MOD to avoid negatives
        return (total - invalid + MOD) % MOD
