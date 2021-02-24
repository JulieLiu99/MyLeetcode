class Solution:
    def makesquare(self, nums: List[int]) -> bool:

        """
        Need to group all nums into 4 sets with equal sums (total/4)
        Time O(n+logn): sort will use logn + dfs traversing through all elements in nums
        Space O(n): array of 4 + used set to hold max n elements from nums
        """
        nums.sort(reverse=True)
        if len(nums) < 4:
            return False
        total = sum(nums)
        if total % 4 != 0:
            return False
        target = total / 4
        if any(n > target for n in nums):
            return False
        return self.dfs([target] * 4, 0, nums)
    

    def dfs(self, targets, idx, nums):
        
        if idx == len(nums):    # has used every stick
            return True 
        
        n = nums[idx]
        used = set()            # to avoid duplicated search
        
        for i in range(4):      # try and see if n belongs to any of the 4 sets
            if targets[i] >= n and targets[i] not in used:
                targets[i] -= n
                if self.dfs(targets, idx + 1, nums):
                    return True
                targets[i] += n
                used.add(targets[i])
                
        return False
        
