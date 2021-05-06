class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        """
        Sort and DP (Bottom Up)
        
        The number of jumps you can make from arr[i] only depends on the array members that are less than arr[i]. 
        Sort the array first and deduce the results of the bigger elements from the smaller ones.
        
        Time O(nd + nlogn)
        Space O(n) to memoize jumps for every index.
        
        """
        valueIndex = sorted([(x, i) for i, x in enumerate(arr)])
        N = len(arr)
        dp = [1] * N
        
        for val, idx in valueIndex[1:]:
                        
            for j in range(1, d+1):
                if idx - j >= 0 and arr[idx - j] < val:
                    dp[idx] = max(dp[idx], dp[idx - j] + 1)
                else:
                    break
                    
            for j in range(1, d+1):
                if idx + j < N and arr[idx + j] < val:
                    dp[idx] = max(dp[idx], dp[idx + j] + 1)
                else:
                    break
        
        return max(dp)



