class Solution:
    def decodeString(self, s: str) -> str:
        """
        We can't just keep a string variable while scanning
        Because k might apply to entire inner structure e.g. "3[a2[c]]"

        Use a stack to store the outer layers, from outer to inner
        Signal for end of existing layer is "["
        stack[i] = [decoded existing string, k for next encoded_string]
        Pop and apply outer layer k when inner is processed, signaled by "]"
        
        Record current k (isdigit)
        Record current string (between [ and ])
        
        Time O(n)
        Space O(1)
        
        """     
        stack = []
        current_string = ""
        k = ""

        for char in s:
            
            if char == "[": # end of digits, start of new encoded_string
                
                # store string and digits from current layer
                # k later applies to entire structure inside the new []
                stack.append((current_string, k))
                k = ""
                current_string = ""
                
            elif char == "]": # end of string, decode current string
                last_string, last_k = stack.pop()
                current_string = last_string + int(last_k) * current_string
                
            elif char.isdigit():
                k += char
                
            else:
                current_string += char

        return current_string