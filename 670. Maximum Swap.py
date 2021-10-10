class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        Swap the frontmost possible digit with a larger value digit after it
        
        -> Keep track of where the digits are, their latest appearance
        -> Go through num from front to end and see if there is a larger digit behind it
        
        Time O(n)
        Space O(n)
        
        """
        num = [i for i in str(num)]
        
        index = collections.defaultdict(int) # last idx of digits 0~9
        for i, c in enumerate(num):
            index[int(c)] = i
            
        for i, c in enumerate(num):
            for k in range(9, int(c), -1):
                if k in index and index[k] > i:
                    num[i], num[index[k]] = num[index[k]], num[i]
                    return int(''.join(num))

        return int(''.join(num))