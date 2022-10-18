class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        3-Sum Approach
        
        Start with largest side
        Find a, b such that sum < c
        
        a + b > c
        b + c > a (we know for sure if c is largest among abc)
        a + c > b (we know for sure if c is largest among abc)
        
        Time O(nlogn)
        Space O(n)
        """
        nums.sort()
        res = 0
        
        # start with largest side
        for c in range(len(nums)-1, 1, -1): # nums[-1] to nums[2]
            a = 0
            b = c - 1
            while a < b:
                if nums[a] + nums[b] > nums[c]:
                    res += b - a
                    b -= 1
                else:
                    a += 1
        return res
