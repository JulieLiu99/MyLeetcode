class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        """
        Brute Force DFS
        
        Search from low digit position to high digit position.
        Stop once (left side sum) % 10 != current digit on the right side.
        
        c = all_words[word_idx][-char_idx-1]
        0 <= char_idx < longest
        
        """
        
        all_words = words + [result]
        
        # can't be 0
        first_chars = set(word[0] for word in all_words if len(word) > 1)
        
        longest = max(map(len, all_words))
        if len(result) < longest: 
            return False
        
        
        def dfs(char_idx, word_idx, carry, visited, char_digit):
            
            # done if reach beyond frontmost digit, with no more carry
            if char_idx == longest: 
                return carry == 0
            
            # have visited the same digit in all words -> check sum
            if word_idx == len(all_words):
                s = 0
                for word in words:
                    if char_idx < len(word):
                        s += char_digit[word[-char_idx - 1]]
                s += carry

                if s % 10 == char_digit[result[-char_idx - 1]]:
                    return dfs(char_idx + 1, 0, s // 10, visited, char_digit)
                else:
                    return False 
                
            # current word length too short to check, move to next word
            if word_idx < len(words) and char_idx >= len(words[word_idx]):
                return dfs(char_idx, word_idx + 1, carry, visited, char_digit)

            c = all_words[word_idx][-char_idx-1]
            
            # if current word's current char already mapped to a digit, continue with next word
            if c in char_digit:
                return dfs(char_idx, word_idx + 1, carry, visited, char_digit)
            
            # otherwise try all possibilities via dfs
            else:
                if c in first_chars:
                    first_digit = 1
                else:
                    first_digit = 0
                    
                for digit in range(first_digit, 10):
                    if digit not in visited:
                        visited.add(digit)
                        char_digit[c] = digit
                        if dfs(char_idx, word_idx + 1, carry, visited, char_digit.copy()): 
                            return True
                        # restore visited and char_digit by discarding the copy
                        visited.remove(digit) 
                return False
            
        return dfs(0, 0, 0, set(), {})
