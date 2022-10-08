class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        Time O(NlogN) for sorting
        Time O(NS^2) for each word, loop through length and generate previous work
        Space O(NS)
        """
        dp = {}
        res = 1

        for word in sorted(words, key=len):
            dp[word] = 1

            # for each word, loop on all possible previous word with 1 letter missing
            for i in range(len(word)):
                prev = word[:i] + word[i + 1:]

                if prev in dp:
                    dp[word] = max(dp[prev] + 1, dp[word])
                    res = max(res, dp[word])

        return res
