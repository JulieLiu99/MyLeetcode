class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        # count consecutive digits in '00110' => [2, 2, 1] 
        # number of valid substring min(2, 2) + min(2, 1) => 3
        
        # Time O(N)
        # Space O(N)
        
        count = [1]
        res = 0

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count[-1] += 1
            else:
                count.append(1)
        
        for a, b in zip(count[:-1], count[1:]):
            res += min(a, b)
            
        return(res)
