class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        count = collections.defaultdict(int)
        i = j = 0
        max_len = 0
        
        while i <= j < len(s):
            count[s[j]] += 1
            while len(count) > k: # remove tail
                count[s[i]] -= 1
                if count[s[i]] == 0: del count[s[i]]
                i += 1
            max_len = max(max_len, j-i+1)
            j += 1
        return max_len
                
