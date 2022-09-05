class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        """
        Count the elements with Counter
        If k > 0, for each element num, check if num + k exist.
        If k == 0, for each element num, check if count[num] > 1

        Time O(N)
        Space O(N)

        """
        res = 0
        counter = collections.Counter(nums)
        for num in counter:
            if (k > 0 and num + k in counter) or (k == 0 and counter[num] > 1):
                res += 1
        return res
