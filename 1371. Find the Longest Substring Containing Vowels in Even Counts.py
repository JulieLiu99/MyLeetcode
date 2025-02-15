class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        """
        Bitmask + Hashtable
        
        State:  Each bit in this bitmask represents whether each vowel occures even (0) or odd (1) times.
        Example 'ue' will be    1    0    0    1    0
                               'u'  'o'  'i'  'e'  'a'
        
        When a vowel occures just flip the bit.
        2^5 = 32 different states.
        
        Use a hashtabke to store the first index of a given state. 
        If the same state occurs again (i -> j), we've found a subarray (i+1 -> j) where all vowels occur even times.
        Length = j - (i+1) + 1 = j - i
        
        Time O(n)
        Space O(32)
        
        """
        
        idx = {0: -1}
        vowels = "aeiou"
        state = 0
        ans = 0
        
        for i in range(len(s)):
            j = vowels.find(s[i])
            if j >= 0:
                state ^= 1 << j
            if state not in idx:
                idx[state] = i
            ans = max(ans, i - idx[state])
            
        return ans
