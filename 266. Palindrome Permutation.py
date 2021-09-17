class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        """
        Matching pairs + 0/1 unmatched char
        
        Keep a set a unmatched chars
        
        Go through the string, check if char in set
            if yes, remove that char
            if no, add that char
            
        In the end, check length of set
            if <= 1, true
            else, false
            
        Time O(n)
        Space O(n)
        
        """
        unmatched = set()
        
        for char in s:
            if char in unmatched:
                unmatched.remove(char)
            else:
                unmatched.add(char)
        
        return len(unmatched) <= 1
