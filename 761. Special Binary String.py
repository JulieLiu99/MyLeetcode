class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        """
        Recursion + Sorting

        Each special substring starts with 1 and ends with 0
        -> Recursively solve the inside part

        Swap for largest value 
        -> Sort special substrings at each recursion level

        Time O(n^2)
        Space O(n)
        """
        subs = []
        count = 0
        i = 0
        for j, ch in enumerate(s):
            if ch == '1':
                count += 1
            else:
                count -= 1
            if count == 0:
                # s[i:j+1] is a special substring
                # Recursively solve the inside part
                subs.append("1" + self.makeLargestSpecial(s[i+1:j]) + "0")
                i = j + 1
        # Sort all special substrings in reverse lex order and join
        subs.sort(reverse=True)
        return ''.join(subs)
