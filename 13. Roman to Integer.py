class Solution:
    def romanToInt(self, s: str) -> int:
        """
        use dictionary and travel backward:
        IV = 4 = 5 - 1
        IX = 9 = 10 -1
        If one letter is less than its latter one, this letter is subtracted.
        
        Time O(n): traverse string once
        Space O(1): one dict + three constants
        
        """
        _dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        prev = 0
        sum = 0
        for i in s[::-1]:
            curr = _dict[i]
            if curr < prev:     # If one letter is less than its latter one,
                sum -= curr     # this letter is subtracted.
            else:
                sum += curr
            prev = curr
        return sum
        
