class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort(reverse = True) # sort in decreasing order by value
        frequency = Counter(nums)
        # sorted(frequency) -> [1, 2, 3] sorted by key
        # sorted(frequency, key = lambda x:frequency[x]) -> [3, 1, 2] sorted by value
        sorted_keys = sorted(frequency, key = lambda x:frequency[x])
        res = []
        for num in sorted_keys:
            res.extend([num] * frequency[num])
        return res
