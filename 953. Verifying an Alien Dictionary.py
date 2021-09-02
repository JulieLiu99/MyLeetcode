class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
        translate words into numeric value
        find largest lenght word
        pad 0s to end of shorter words -> this is wrong because 1~26 some can be two digits
        -> have to calculate actual numeric values
        -> calculated value *= 10 to the power of (max_length - len(word))
        
        go through the list of numeric values
        if prev < cur: continue
        else: return false
        
        Time O(n * m): for each word, for each char
        Space O(n + 26): dic O(26), vals O(n)
        
        """
#         dic = {}
#         for i, char in enumerate(order):
#             dic[char] = i+1     # value from 1 onwards
        
#         vals = []
#         max_length = 0
#         for word in words:
#             max_length = max(max_length, len(word))
#             val = 0
#             for i, char in enumerate(reversed(word)):
#                 val += dic[char] * pow(10, i)
#             vals.append(val)
            
#         pre = vals[0] * pow(10, (max_length - len(words[0])))
#         for j in range(1, len(words)):
#             cur = vals[j] * pow(10, (max_length - len(words[j])))
#             if cur >= pre:
#                 pre = cur
#             else:
#                 return False
            
#         return True

        """
        Can directly compare two lists in Python
        [1,1,1] > [1,1], [1,3] > [1,1,1]
        
        Same complexities
        """
        dic = {}
        for i, char in enumerate(order):
            dic[char] = i
            
        vals = []
        for word in words:
            val = []
            for char in word:
                val.append(dic[char])
            vals.append(val)
        
        pre = vals[0]
        for cur in vals:
            if cur >= pre:
                pre = cur
            else:
                return False
            
        return True
