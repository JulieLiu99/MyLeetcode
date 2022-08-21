class Solution:
    def largestVariance(self, s: str) -> int:
        
        # DP
        # dp[i] is max subarray ending at i that contains positive variance for a char
        
        # Time O(26 * 25 * n) = O(n)
        # Space O(n)

        counter = Counter(s)
        res = 0
        
        # Get variance for each pair of characters
        # permutation because for each (a, b) we are getting variance for a only
        
        for a, b in itertools.permutations(counter, 2):
            max_subarray = 0
            has_a, has_b = False, False
            remain_a, remain_b = counter[a], counter[b]
            
            # dp[i] = max(dp[i-1], 0) + s[i]
            for char in s:
                if char != a and char != b:
                    continue
                # if dp[i-1] < 0, start with new substring
                # only restart if there are a's and b's in rest of the string
                if max_subarray < 0 and remain_a != 0 and remain_b != 0:
                    max_subarray=0
                    has_a, has_b = False, False
                # add to existing substring
                if char == a: 
                    max_subarray += 1
                    remain_a -= 1
                    has_a = True
                elif char == b: 
                    max_subarray -= 1
                    remain_b -= 1
                    has_b = True
                # to prevent "ab" from giving 1 after seeing just "a"
                if has_a and has_b:
                    res = max(res, max_subarray)
        return res
