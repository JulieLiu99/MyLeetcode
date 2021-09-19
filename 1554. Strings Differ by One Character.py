class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        """
        Brute Force: 
        
        For each string, compare it with every other string. If differ by 1, return.
        
        Time O(n^2 * len(string))
        Space O(1)
        
        """
        
        """
        Store all the patterns seen
        Pattern = for each word, replace one char with "*"
        Whenever we come across a pattern that been seeen previously -> It's a MATCH!
        
        Time O(n * len(string))
        Space O(n* len(string))
        
        """
        seen = set()
        for word in dict: 
            for i in range(len(word)): 
                pattern = word[:i] + "*" + word[i+1:]
                if pattern in seen: 
                    return True 
                seen.add(pattern)
        return False
