class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Going forward. 
        reach = the maximum index we can reach so far.
        
        https://www.youtube.com/watch?v=muDPTDrpS28
        
        Time O(n)
        Space O(1)
        
        """
        reach = 0
        for i, num in enumerate(nums):
            if reach < i: # current reacheable cannot reach i
                return False
            reach = max(reach, i+num)
        return True
