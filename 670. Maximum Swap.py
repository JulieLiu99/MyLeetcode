class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        Swap the frontmost possible digit with a larger value digit after it
        
        -> Keep track of where the digits are, their latest appearance
        -> Go through num from front to end and see if there is a larger digit behind it
        
        Time O(n)
        Space O(n)
        
        """
        tracker = collections.defaultdict(int) # keep track of last idx of digits 0~9
      
        num = [i for i in str(num)]
        
        for i, c in enumerate(num):
            tracker[int(c)] = i
            
        for i, c in enumerate(num):
            for k in range(9, -1, -1):
                if k > int(c) and tracker[k] > i:
                    num[i], num[tracker[k]] = num[tracker[k]], num[i]
                    return int(''.join(num))

        return int(''.join(num))
