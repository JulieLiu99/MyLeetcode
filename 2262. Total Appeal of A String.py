class Solution:
    def appealSum(self, s: str) -> int:
        
#         For each character s[i],
#         the substring must start before s[i] to contain s[i]
#         and need to end after the last occurrence of s[i],
#         otherwise the last occurrence of character s[i] will get the socre.

#         In total, there are i - last[s[i]] possible start position,
#         and n - i possible end position,
#         so s[i] can contribute (i - last[s[i]]) * (n - i) points.

#         Complexity: Time O(n), Space O(26)
        
        last = defaultdict(lambda: -1)
        n = len(s)
        res = 0
        
        for i, c in enumerate(s):
            res += (i - last[c]) * (n - i)
            last[c] = i
            
        return res
