class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
          1  2  3
        * 4  5  6
        ----------
        6 * 123 + 5 * 123 * 10 + 4 * 123 * 100
        
        Important observation is that the length of multiplication result 
        = lenght of num1 + length of num2  
    
        (0.N * 10^n) * (0.M * 10^m) = 0.M * 0.N * 10^(m+n)
        e.g. 2 = 0.2 * 10^1
             19 = 0.19 * 10^2
             2 * 19 = 0.2 * 0.19 * 10^3
        
        """
        
        n, m = len(num1), len(num2)
        if not n or not m:
            return "0"
        
        result = [0] * (n + m)
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                 # current =  0 + 3 * 6
                 #            1 + 3 * 5
                 #            1 + 3 * 4
                 #            6 + 2 * 6
                 #            4 + 2 * 5
                 #            2 + 2 * 4
                 #            4 + 1 * 6
                 #            1 + 1 * 5
                 #            1 + 1 * 4
                current = int(result[i + j + 1]) + int(num1[i]) * int(num2[j])
                result[i + j + 1] = current % 10
                result[i + j] += current // 10
        
        for i, c in enumerate(result):
            if c != 0:
                # map() function applies the given function to each item of a given iterable.
                return "".join(map(str, result[i:]))
        
        return "0"
