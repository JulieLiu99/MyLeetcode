class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        
        """
        First, we cannot change root, otherwise different tree
        
        Second, nodes in the left < root, nodes in the right > root
        l = [x for x in nums if x < nums[0]]
        r = [x for x in nums if x > nums[0]]
        
        Interleaving l and r will lead to the same tree
        There are C(|l|+|r|, |l|) ways
        
        Do it recursively for l and r
        
        Total ways = C(|l|+|r|, |l|) * way(l) * way(r)
        Return = Total ways - 1
        
        Time O(nlogn) best, O(n^2) worst
        Space O(nlogn) best, O(n^2) worst
        """
        
        def way(nums):
            if len(nums) <= 2: return 1
            l = [x for x in nums if x < nums[0]]
            r = [x for x in nums if x > nums[0]]
            return comb(len(l)+len(r), len(r)) * way(l) * way(r)
        return (way(nums)-1) % (10**9+7)
