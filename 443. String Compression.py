class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        One traversal of string
        Pointers (next read, length of repeated sequence, next position to write to)
        """
        n = len(chars)
        i = 0
        write = 0 # pointer for next position to write into
        while i < n:
            char = chars[i]
            length = 1
            while i + 1 < n and char == chars[i+1]:
                length += 1
                i += 1
            chars[write] = char
            write += 1
            if length > 1:
                for digit in str(length):
                    chars[write] = digit
                    write += 1
            i += 1 # next different char
        return write


