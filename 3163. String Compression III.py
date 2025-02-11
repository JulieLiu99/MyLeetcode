class Solution:
    def compressedString(self, word: str) -> str:
        """
        One pointer traverses the string
        Time O(n)
        Space O(n)
        """

        comp = ""
        i = 0

        while i < len(word):

            char = word[i]
            count = 0

            # Count consecutive occurrences (maximum 9)
            while (
                i < len(word)
                and count < 9
                and word[i] == char
            ):
                count += 1
                i += 1

            comp += (str(count) + char)

        return comp