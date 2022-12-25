class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        """
        We only care about sum of subsequence: order does not matter!
        -> get the sum of the smallest nums

        Sort + Prefix sum + Binary search

        Time O(nlogn + n + mlogn)
        Space O(n)

        We could also use: Sort + Linear scan each query
        Time O(nlogn + mn)
        """
        sorted_nums = sorted(nums) # ascending order

        prefix_sum = [0] # prefix_sum[i]: sum till sorted_nums[i-1]
        for num in sorted_nums:
            prefix_sum.append(prefix_sum[-1] + num)

        res = [] 
        # binary search for each query: sums=[0, 1, 2], query=2 -> res=3
        for query in queries:
            res.append(bisect.bisect_right(prefix_sum, query)-1)

        return res


