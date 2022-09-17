class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openning = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in openning.values():
                stack.append(char)
            elif char in openning.keys():
                if stack == [] or openning[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
