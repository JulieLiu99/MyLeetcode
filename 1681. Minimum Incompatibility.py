class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        
        """
        DFS Recursion
        
        Easy to TLE, unless with @lru_cache(None) and dfs(tuple(nums))
        
        """
#         groupsize = len(nums)//k

#         @lru_cache(None)
#         def dfs(nums):
#             if not nums:
#                 return 0
#             res = float('inf')
#             for combs in combinations(nums, groupsize):
#                 if len(combs) != len(set(combs)): # not unique
#                     continue
#                 nxt_nums = list(nums)
#                 for cand in combs:
#                     nxt_nums.remove(cand)
#                 res = min(res, max(combs) - min(combs) + dfs(tuple(nxt_nums)))
#             return res
        
#         res = dfs(tuple(nums)) # turn the input into a tuple so the function can be cached
#         return res if res != float('inf') else -1
    
        """
        Bitmask DP
        
        dp[mask][i]: min cost to distribute numbers (as a binary mask) when the last number is i.
        
        Init:
        
        dp[1 << i][i] = 0       # cost of selecting a single number is zero
        
        Transition:
        
        1) Start a new group
        dp[mask | (1 << j)][j] = dp[mask][i]
        Use permutation because we can choose any num, not neccecerily bigger than previous

        2) Extend the current group 
        dp[mask | (1 << j)][j] = dp[mask][i] + nums[j] - nums[i]
        Use combination because next index should be bigger than previous.
        
        How to caputre max - min? 
        Make all groups monotonically increasing (automatically done by permuation and combination too).
        
        Ans:
        
        min(dp[(1 << n) - 1])
        
        Time O(2^n * n^2): we have 2^n bitmasks, and O(n^2) time to process each bitmask. 
        Space O(2^n * n)
        
        """
        n = len(nums)
        if k == n: return 0
        
        dp = [[float("inf")] * n for _ in range(1<<n)] 
        nums.sort()
        groupsize = len(nums) // k
        
        for i in range(n): 
            dp[1<<i][i] = 0

        for mask in range(1<<n):
            n_z_bits = [j for j in range(n) if mask&(1<<j)]
            print(bin(mask), n_z_bits)
            if len(n_z_bits) % groupsize == 1:
                for j, l in permutations(n_z_bits, 2):
                    # e.g. 0b111111 -> 0b111011 for l = 2
                    dp[mask][l] = min(dp[mask][l], dp[mask^(1<<l)][j])
            else:
                for j, l in combinations(n_z_bits, 2):
                    if nums[j] != nums[l]:
                        dp[mask][j] = min(dp[mask][j], dp[mask^(1<<j)][l] + nums[l] - nums[j])
                        
        return min(dp[-1]) if min(dp[-1]) != float("inf") else -1
