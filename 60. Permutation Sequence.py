class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        for digit in 1...n
        there are (n-1)! permutations that starts with this digit
        k//(n-1)! to determine the first digit
        
        then k//(n-2)! for the next digit
        
        Time O(n^2)
        Space O(n)
        
        """
        
        def factorial(n):
            if n == 1 or n == 0:
                return 1
            return n*factorial(n-1)
        
        res = ""
        taken = set({0})
        
        for i in range(n):
            
            digit_group_size = factorial(n-i-1)
            digit = k//digit_group_size
            

            # if no reminder, stay in previous digit group
            if k % digit_group_size == 0: 
                digit -= 1
                k -= digit * digit_group_size
            else:
                k %= digit_group_size
                
            # skip digits already taken
            x = 0
            while x < digit:
                if x in taken:
                    digit += 1
                x += 1
            while digit in taken:
                digit += 1
                
            taken.add(digit)
            res += str(digit)
        
        return res
