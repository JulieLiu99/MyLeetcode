class Solution:
    def findComplement(self, num: int) -> int:
        bi = str(bin(num))[2:]
        complement = []
        for i, c in enumerate(bi):
            if c == "1":
                complement += [0]
            if c == "0":
                complement += [1]
        res = 0
        pwr = 0
        for i in range(len(complement)-1, -1, -1):
            if complement[i]:
                res += 2 ** pwr
            pwr += 1
        return res
            
