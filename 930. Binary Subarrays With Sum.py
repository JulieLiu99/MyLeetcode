class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        Sliding Window
        
        Time O(N)
        Space O(1)
        
        """
        l = 0
        l_count = 0
        res = 0
        s = 0
        for r, num in enumerate(nums):
            s += num
            if num == 1:
                l_count = 0
            while l<= r and s >= goal:
                if s == goal:
                    l_count += 1
                s -= nums[l]
                l += 1
            res += l_count
        return res
    
        """
        Hash + Prefix Sum
        
        Count the occurrence of all prefix sum.

        This solution also works if there are negatives.

        Time O(N)
        Space O(N)
        
        """
        # count = collections.Counter({0: 1})
        # psum = 0
        # res = 0
        # for num in nums:
        #     psum += num
        #     res += count[psum - goal]
        #     count[psum] += 1
        # return res
