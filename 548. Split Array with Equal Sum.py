class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        """
        Brute Force:
        Time O(n^3)
        
        for i ...
            for j ...
                if sum(0, i-1) == sum(i+1, j-1):
                    for k ...
                    
        This could be redundant because need to search on k for many i, j pairs
        50000000050
          ii...   j
        
        
        Optimization: 
        for j ...
            find i that splits left half evenly
            find k that splits right half evenly
            
        Time O(n)
        Space O(1)
        
        [1,2,1,2,1,2,1]
         0 1 2 3 4 5 6,  n = 7
           i   j   k
           
        """
        if not nums: return False
        
        n = len(nums)
        presum = [nums[0]]
        for num in nums[1:]:
            presum.append(presum[-1] + num)
        
        for j in range(3, n-3): # explore mid point
            targets = set()
            
            for i in range(1, j-1): # splitting left
                if presum[i-1] == presum[j-1] - presum[i]:
                    targets.add(presum[i-1])
            
            for k in range(j+2, n-1): # splitting right
                if presum[n-1] -  presum[k] == presum[k-1] - presum[j] and  (presum[k-1] - presum[j] in targets):
                    return True
        
        return False
