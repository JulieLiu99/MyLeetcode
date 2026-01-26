class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        Go through the word and abbr together
        
        If abbr has a number x, go forward in word by x
        
        Whenever don't match, return False
        
        Time O(n)
        Space O(1)
        
        "i nternational iz atio n"
        "i 12 iz 4 n"
        
        "a"
        "2"
        Corner case: if number is in the end but not a right number
        """
        i = j = 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isdigit():
                if abbr[j] == "0": return False  # number can't start with 0
                x = int(abbr[j])
                while j + 1 < len(abbr) and abbr[j+1].isdigit(): 
                    j += 1
                    x = x * 10 + int(abbr[j])
                j += 1
                i += x
            else:
                return False

        if i != len(word) or j != len(abbr): # not exactly match
            return False
        return True
