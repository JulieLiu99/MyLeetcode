class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Greedy 
        
        l, r: current reacheable window
        
        Time O(n)
        Space O(1)

        """

        times = 0
        l = r = 0
        
        while r < len(nums)-1:
            reach = 0
            for i in range(l, r + 1):
                reach = max(reach, i + nums[i])
            l = r + 1
            r = reach
            times += 1
            
        return times
