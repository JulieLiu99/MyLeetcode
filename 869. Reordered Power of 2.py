class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        """
        Two numbers are permutations iff their sorted digit strings match

        Enumerate all powers of 2 that could match n and compare
        (from 2^0 to 2^30, which covers up to 10 digits since n ≤ 10^9)
        
        Time: O(d log d) for sorting
        Space: O(d) to store the digit
        """
        def shorted_digits(x):
            return ''.join(sorted(str(x)))

        target = shorted_digits(n)
        
        for i in range(31):
            if shorted_digits(1 << i) == target:
                return True
        return False
