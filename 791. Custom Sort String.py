class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        Go through order and search for all matching chars in s 
        
        Go through s and store {char:counts} first to make search O(1)
        
        Append all else to the end
        
        Time O(len(s) + len(order))
        Space O(len(s))
        
        """
        counter = collections.Counter(s)
        res = ""
        
        for char in order:
            if char in counter:
                res += char * counter[char]
                del counter[char]
                
        for char in counter:  # chars not in order
            res += char * counter[char]
            
        return res
