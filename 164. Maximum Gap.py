class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        """
        Bucket Sort
        
        1) Create n empty buckets (Or lists).
        2) Do following for every array element arr[i].
        .......a) Insert arr[i] into bucket[n*array[i]]
        3) Sort individual buckets using insertion sort. (Not used in this problem.)
        4) Concatenate all sorted buckets.
        
        We want to make sure those two numbers forming the maximum difference fall into separate buckets so that we do not need to worry about the numbers in the same bucket. To achieve this we want the size of each bucket to be less than the maximum difference.

        Let size denote the maximum difference, then we have size * (len(nums)-1) >= b - a, so size >= (b-a) / (len(nums)-1). Since size must be integer, we get size >= math.ceil((b-a) / (len(nums)-1)). Thus we make size = math.ceil((b-a) / (len(nums)-1)).

        Then by making the number of buckets to be (b - a) // size + 1, it is guaranteed that the final bucket size is less than maximum difference. Hence the two numbers forming maximum difference will be in separate buckets.

        Finally, we find the maximum difference between two adjacent buckets (min value of current bucket and max value of previous bucket) and that will be the answer.
        
        Time O(N)
        Space O(N)
        
        """
        
        if len(nums) < 2 or min(nums) == max(nums):
            return 0
        
        a, b = min(nums), max(nums)
        size = (b-a)//(len(nums)-1) or 1
        bucket = [[None, None] for _ in range((b-a)//size+1)]
        
        for num in nums:
            b = bucket[(num-a)//size]
            b[0] = num if b[0] is None else min(b[0], num)
            b[1] = num if b[1] is None else max(b[1], num)
        bucket = [b for b in bucket if b[0] is not None]
        
        return max(bucket[i][0]-bucket[i-1][1] for i in range(1, len(bucket)))
