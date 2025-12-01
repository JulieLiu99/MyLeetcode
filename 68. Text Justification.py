class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        """
        Time O(n)
        Space O(1)
        
        """
        
        c_counter = 0 # character counter
        w_counter = 0 # word counter
        res = []
        
        for word in words:
            
            # new line
            if c_counter == 0:
                res.append(word)
                c_counter += len(word)
                w_counter += 1
                
            # add word to existing line
            elif c_counter + len(word) + 1 <= maxWidth:
                res[-1] += " " + word
                c_counter += len(word) + 1
                w_counter += 1
                
            # line full, handle extra space
            else:
                extra_space = maxWidth - c_counter

                # if multiple words, distribute space
                if extra_space and w_counter > 1:
                    gaps = w_counter - 1
                    even_space = extra_space // gaps
                    extra_slots = extra_space % gaps

                    i = 1
                    while i < len(res[-1]):
                        if res[-1][i] == " " and res[-1][i-1] != " ": # gap
                            if extra_slots > 0:
                                insert = " " * (even_space + 1)
                                extra_slots -= 1
                            else:
                                insert = " " * even_space
                            res[-1] = res[-1][:i] + insert + res[-1][i:]
                            i += len(insert)
                        i += 1

                # if only one word, append space to right
                elif extra_space and w_counter == 1:
                    res[-1] += " " * extra_space
                
                # add word to new line
                res.append(word)
                c_counter = len(word)
                w_counter = 1
                
        # handle extra space in last line
        extra_space = maxWidth - c_counter
        if extra_space:
            res[-1] += " " * extra_space
                
        return res
