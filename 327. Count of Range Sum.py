class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        """
        Binary Indexed Tree
        
        Range_Sum = Sum[j] - Sum[i-1]
        lower <= Sum[j] - Sum[i-1] <= upper
        
        nums        [X X X X X X]
                       i-----j
        sortSum   [0 X X X X X X]
        BITree  [0 0 X X X X X X]
        
        For every Sum[j] from large to small:     
            Count i that satisfies: 
            - Sum[i-1] <= Sum[j] - lower
            - Sum[i-1] >= Sum[j] - upper
        
        Store the index of sortSum in the BITree. 
        
        Time O(NlogN): 
            counting sum_i number is O(logN);
            putting sum_i into tree is also O(logN).
        Space O(N)
        
        """
        
        n = len(nums)
        Sum = [0] * (n + 1)
        BITree = [0] * (n + 2)

        def addCount(x):
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
            
            # bisect.bisect_right(sortSum, sum_j - lower) returns the right-most index
            # So that all sums from 0 to index-1 inclusive will be <= sum_j - lower. 
            # The count for those sums would be addCount(index - 1 + 1). 
            # Similarly,
            # bisect.bisect_left(sortSum, sum_j - upper) returns left-most index
            # So that all sums from index+1 to end inclusive will be >= sum_j - upper. 
            
            sum_i_count = addCount(bisect.bisect_right(sortSum, sum_j - lower)) -             
                          addCount(bisect.bisect_left(sortSum, sum_j - upper))
            res += sum_i_count
            
            # Since index of BITree starts from 1, 
            # we need bisect.bisect_left(sortSum, sum_j) + 1 for update().
            update(bisect.bisect_left(sortSum, sum_j) + 1)
            
        return res