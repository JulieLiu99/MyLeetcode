class Solution:
    def decodeString(self, s: str) -> str:
        """
        Go through the string
        
        Stack
        stack[i] = [string, count]
        
        Record current count (isdigit)
        Record current string (between [ and ])
        
        Time O(n)
        Space O(1)
        
        """
        
        stack = []
        current_string = ""
        k = 0

        for char in s:
            if char == "[":
                stack.append((current_string, k))
                current_string = ""
                k = 0
            elif char == "]":
                last_string, last_k = stack.pop()
                current_string = last_string + last_k * current_string
            elif char.isdigit():
                k = k * 10 + int(char)
            else:
                current_string += char

        return current_string
