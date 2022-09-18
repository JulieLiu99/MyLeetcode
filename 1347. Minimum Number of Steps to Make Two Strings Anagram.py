class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # Count occurrences and return the number of unmatched chars
        count = collections.Counter(s)
        res = 0
        for char in t:
            if count[char] > 0:
                count[char] -= 1
            else:
                res += 1
        return res
