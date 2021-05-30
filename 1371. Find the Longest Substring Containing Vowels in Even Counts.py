class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        """
        Hashtable
        
        State: prefix sum => prefix freq
        whether each vowel occures even (0) or odd (1) times.
        
        When a vowel occures we just flip the bit.
        
        01110 =  u_even o_odd i_odd e_odd a_even
        2^5 = 32 different states
        
        Use a hashtabke to store the first index of a given state. 
        If the same state occurs again (i -> j), we've found a subarray (i+1 -> j) where all vowels occur even times.
        Length = j - (i+1) = j - i
        
        [e[baa]e]
        len = 3, s = "baa"
        len = 4, s = "ebaae"
        
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
