class Solution:
    def numberOfArrays(
        self, differences: List[int], lower: int, upper: int
    ) -> int:
        """
        lower bound <= smallest value <= largest value <= upper bound

        Get the number of positions where a small window of length (largest - smallest) 
        can be placed while sliding within a large window of length (upper − lower)

        solution = large window size - small window size + 1
        e.g. 4 - 2 + 1 = 3 
        1 2 3 4 
        ^ ^
          ^ ^
            ^ ^

        Time O(n)
        Space O(1)
        """
        smallest = 0
        largest = 0 
        cur = 0

        for diff in differences:
            cur += diff
            smallest = min(smallest, cur)
            largest = max(largest, cur)
            if largest - smallest > upper - lower: # impossible
                return 0

        return (upper - lower) - (largest - smallest) + 1
