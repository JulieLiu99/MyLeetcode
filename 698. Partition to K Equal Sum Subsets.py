class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        """
        DFS
        
        Time O(n^k): for each number in nums, decide which target slot it belongs to
        Space O(n^k)
        
        """
        
        if len(nums) < k:
            return False
        
        s = sum(nums)
        if s % k != 0: 
            return False
        
        nums.sort(reverse=True)
        targets = [s / k] * k

        def dfs(i):
            
            if i == len(nums): return True
            
            for subset in range(k):
                if targets[subset] >= nums[i]:
                    targets[subset] -= nums[i]
                    if dfs(i + 1):
                        return True
                    targets[subset] += nums[i]
                    
            return False
        
        return dfs(0)
