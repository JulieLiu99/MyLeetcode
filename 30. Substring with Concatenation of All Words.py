class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        Sliding Window
        
        Use a counter and a sliding window, push the window from left to right, and count the number of valid words in the window. 
        When the number of a word in the window is more than the times it appears in words or we meet a invalid word, push the window.
        
        Time O(n #words #substrings) where n=len(s): we need to adjust the window when more valid words are found.
        Space O(n)
        
        """
        n = len(words)
        word_l = len(words[0])
        counter = {}
        ans = []
        
        if n == 0:
            return []
        
        for word in words:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1

        # Loop over first word length
        for i in range(word_l):
            start = i
            sub_counter = defaultdict(int)
            count = 0
            
            # Loop over the string
            for j in range(i, len(s)-word_l+1, word_l):
                word = s[j:j+word_l]
                
                # Check if it is a valid word
                if word in counter:
                    sub_counter[word] += 1
                    count += 1
                    
                    # Shift the window as long as we have encountered 
                    # more number of a word than needed
                    while sub_counter[word] > counter[word]:
                        sub_counter[s[start:start+word_l]] -= 1
                        start += word_l
                        count -= 1
                        
                    # Count will be equal to len(words) only when 
                    # all the words are read the exact number of times needed
                    if count == n:
                        ans.append(start)
                        
                # If not a valid word
                # skip over the current word
                else:
                    start = j + word_l
                    sub_counter = defaultdict(int)
                    count = 0

        return ans
