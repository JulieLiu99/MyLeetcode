class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        """
        Ternary representation
        Same as binary representation but with base 3 instead of 2

        Take n = 91

        91 % 3 = 1 → ok, keep going. n = 30
        30 % 3 = 0 → ok, keep going. n = 10
        10 % 3 = 1 → ok, keep going. n = 3
         3 % 3 = 0 → ok, keep going. n = 1
         1 % 3 = 1 → ok, keep going. n = 0

        91 = 81 + _ +  9  + _ + 1 
           = 3⁴ + _ +  3² + _ + 3⁰

        Time O(log_3 n)
        Space O(1)
        """
        while n > 0:
            if n % 3 == 2: # each power can only be present (1) or non present (0)
                return False
            # move to the next greater power
            n //= 3
        return True
