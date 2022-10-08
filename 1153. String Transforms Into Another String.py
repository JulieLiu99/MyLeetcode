class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        """
        Explanation for len(set(str2)) < 26:
        
        Let's say we have an alphabet of "abc".
        To transform "ab" to "ba": "cb" -> "ca" -> "ba" 
        We use "c" as a temporary comversion while converting "a" to "b".
        
        However, if we only have an alphebet of "ab".
        To transform "ab" to "ba": "bb" -> CANNOT proceed anymore!
        There IS another char that's same as conversion for current char -> if use this conversion we break string pattern
        """
        
        if str1 == str2:
            return True
        
        m = {} # mapping of characters
        
        for char1, char2 in zip(str1, str2):
            
            if char1 not in m:
                m[char1] = char2
                
            elif m[char1] != char2: # violation of existing mapping
                return False
            
        return len(set(str2)) < 26 # we need at least one char for temp conversion
