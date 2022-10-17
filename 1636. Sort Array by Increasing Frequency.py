class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = Counter(nums)
        #  increasing order based on the frequency
        #  decreasing order based on value
        sorted_keys = sorted(frequency, key = lambda num: (frequency[num], -num))
        res = []
        for num in sorted_keys:
            res.extend([num] * frequency[num])
        return res
        