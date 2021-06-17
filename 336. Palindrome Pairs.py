class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        """
        Keep a reversed string set.
        For each word, check if can find valid pair from the set.
        
        1) Append both sides:       bag, gab  -> baggab, gabbag
        2) Append on right side:    race, car -> racecar  (rac e car)
        3) Append on left side:     run, nu   -> nurun    (nu r un)
        
        Time O(n*L^2), where n is the number of words in the dict, L is the average length of each word.
        Space O(n)
        
        """
        
        reverse_i = dict([(word[::-1], i) for i, word in enumerate(words)])
        res = []
        
        # loop through all words
        for i, word in enumerate(words):
            
            # for each current word, split it across its length
            for j in range(len(word)+1):    
                
                # j = 0, ..., len(word)
                # prefix = word[0...j-1]            ->  [] to word
                # postfix = word[j...len(words)-1]  ->  word to []
                
                prefix = word[:j]   
                postfix = word[j:]  
                
                # Check if can append the other word to the BACK of current word
                # 1. there is word that is reverse of the first half
                # 2. and the reverse word is not itself (because we need a pair)
                # 3. and the remaining half is palindrome on its own (so that ok to keep in the middle)
                if prefix in reverse_i and i != reverse_i[prefix] and postfix == postfix[::-1]:
                    res.append([i, reverse_i[prefix]])
                    
                # Check if can append the other word to the FRONT of current word
                # 1. if there is nonempty first half (if entire word, handled already as BACK)
                
                # ["abcd","dcba","lls","s","sssll"]
                # "dcbaabcd","abcddcba","slls","llssssll"
                
                # back)  abcd dcba
                # back)  dcba abcd
                # front) s lls
                # front) lls sssll
                
                # 2. and there is word that is reverse of the first half
                # 4. and the reverse word is not itself (because we need a pair)
                # 5. and the first half is palindrome on its own (so that ok to keep in the middle)
                if j>0 and postfix in reverse_i and i != reverse_i[postfix] and prefix == prefix[::-1]:
                    res.append([reverse_i[postfix], i])
                    
        return res 
