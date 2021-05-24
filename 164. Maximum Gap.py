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
        
        Assuming interval denotes max range in each bucket, we have interval * (len(nums) - 1) >= max_num - min_num, so interval >= (max_num - min_num) / (len(nums) - 1). Since interval must be integer, we get interval >= math.ceil((max_num - min_num) / (len(nums) - 1)). So we make smallest max range interval = math.ceil((max_num - min_num) / (len(nums) - 1)).

        So we make the number of buckets to be  (max_num - min_num)//interval + 1, it is guaranteed that the final bucket interval is less than maximum difference. Hence the two numbers forming maximum difference will be in separate buckets.

        Finally, we find the maximum difference between two adjacent buckets (min value of current bucket and max value of previous bucket) and that will be the answer.
        
        Time O(N)
        Space O(N)
        
        """
        
        if len(nums) < 2: 
            return 0
        
        min_num = min(nums) 
        max_num = max(nums)
        if min_num == max_num: 
            return 0
        
        interval = math.ceil((max_num - min_num) / (len(nums) - 1))
        
        # buckets[min, max]
        buckets = [[None, None] for _ in range((max_num - min_num)//interval + 1)]
        
        for num in nums:
            b = buckets[(num - min_num)//interval]
            b[0] = num if b[0] is None else min(b[0], num)
            b[1] = num if b[1] is None else max(b[1], num)
        
        buckets = [b for b in buckets if b[0] is not None]
        
        return max(buckets[i][0] - buckets[i-1][1] for i in range(1, len(buckets)))
