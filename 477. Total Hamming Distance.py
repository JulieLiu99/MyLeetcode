class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        """
        for each num
        00011
        count the 0's (3) and the 1's (2), multiply = 3 * 2 = 6 different pairs
        
        Time O(mn)
        Space O(32)
        
        """
        l = len(nums)
        bits_count = [0] * 32

        for num in nums:
            idx = 0
            while num > 0:
                if num & 1 == 1:
                    bits_count[idx] += 1
                num >>= 1
                idx += 1
        return sum([x * (l-x) for x in bits_count])
