class Solution:
    """
    Fenwick Tree/ Binary Indexed Tree
    
    https://www.youtube.com/watch?v=2SVLYsq5W8M&t=1082s
    https://www.youtube.com/watch?v=v_wj_mOAlig
    
    Prefix sums of prequencies
    convert the number to its rank as in sorted array
    sorted [1, 2, 5, 6]
    input  [1, 6, 2 5]
    ranks  [1, 4, 2, 3]
    
    Increase freq[rank] by 1
    
    Time O(nlogn)
    Space O(k), k is # of unique elements
    
    """
    def countSmaller(self, nums: List[int]) -> List[int]:
        rank = {val: i+1 for i, val in enumerate(sorted(nums))}
        N = len(nums)
        tree = [0] * (N+1)
        res = []

        def update(i):
            while i <= N:
                tree[i] += 1
                i += (i & -i) # least significant bit

        def getSum(i):
            s = 0
            while i:
                s += tree[i]
                i -= (i & -i)
            return s

        for num in reversed(nums):
            res.append(getSum(rank[num]-1)) # get sum of all previous numbers
            update(rank[num])
        return res[::-1] # reverse
