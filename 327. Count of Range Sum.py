class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        """
        Binary Indexed Tree
        
        Range_Sum = Sum[j] - Sum[i-1]
        lower <= Sum[j] - Sum[i-1] <= upper
        
        Find i so that: 
        - Sump[j] >= Sum[i-1] + lower => count of larger numbers after self
        - Sump[j] <= Sum[i-1] + upper => count of smaller numbers after self
        
        Store the index of sortSum in the BITree. 
        
        Time O(NlogN): 
            counting sum_i number is O(logN);
            putting sum_i into tree is also O(logN).
        Space O(N)
        
        """
        
        n = len(nums)
        Sum = [0] * (n + 1)
        BITree = [0] * (n + 2)

        def addSum(x):
            s = 0
            while x:
                s += BITree[x]
                x -= (x & -x)
            return s

        def update(x):
            while x <= n + 1:
                BITree[x] += 1
                x += (x & -x)

        for i in range(n):
            Sum[i+1] = Sum[i] + nums[i]
            
        sortSum = sorted(Sum) # descending
        res = 0
        
        for sum_j in Sum:
            
            # bisect.bisect_right(sortSum, sum_j - lower) returns the smallest index that sortSum[ind] >= sum_j - lower. 
            # bisect.bisect_left(sortSum, sum_j - upper) returns the largest index that sortSum[ind] <= sum_j - upper. 
            # So all sums from index 0 to ind-1 inclusive will be <= sum_j - lower. 
            # The count for those sums would be search(ind - 1 + 1). 
            
            sum_i_count = addSum(bisect.bisect_right(sortSum, sum_j - lower)) -                                         addSum(bisect.bisect_left(sortSum, sum_j - upper))
            res += sum_i_count
            
            # Since index of BITree starts from 1, 
            # we need bisect.bisect_left(sortSum, sum_j) + 1 for update().
            update(bisect.bisect_left(sortSum, sum_j) + 1)
            
        return res
