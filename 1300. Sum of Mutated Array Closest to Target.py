class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        """
        Binary Search
        
        Time O(N + log(max(arr)))
        Space O(N)
        
        """
        def getSum(val):
            i = bisect.bisect_right(arr, val)
            if i == 0:
                return (len(arr)-i) * val
            else:
                return preSum[i-1] + (len(arr)-i) * val
            
        arr.sort()
        preSum = arr[:]
        for i in range(1, len(arr)):
            preSum[i] += preSum[i-1]
            
        l = 0
        r = max(arr)
        
        while l <= r:
            m = l + (r - l) // 2
            s = getSum(m)
            if s == target:
                return m
            elif s < target:
                l = m + 1
            else:
                r = m - 1
            
        if abs(getSum(l) - target) < abs(getSum(r) - target):
            return l
        else:
            return r


