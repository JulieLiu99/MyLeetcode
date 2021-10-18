class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        DFS (top down)
        
        For each day, try buying different passes
        
        Keep track of how much money spent to complete all travels
        Return the minimum money spent
        
        Time O(3 ^ len(days))
        Space O(3 ^ len(days))
        
        """
        """
        TLE
        
        """
#         res = float("inf")
        
#         @lru_cache(None)
#         def dfs(i, money):
#             nonlocal res
#             if i == len(days):
#                 res = min(res, money)
            
#             for cost, cover in zip(costs, [1,7,30]):
#                 j = i
#                 while j < len(days) and days[j] < days[i] + cover:
#                     j += 1
#                 dfs(j, money + cost)
                
#         dfs(0, 0)
#         return res
    
        """
        Top down recursion + memorization
        
        """
        n = len(days)
        
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            
            if i == n:
                return 0
            
            res = float('inf')
            for cost, cover in zip(costs, [1, 7, 30]):
                j = i
                while j < n and days[j] < days[i] + cover:
                    j += 1
                res = min(res, cost + dfs(j))
            
            memo[i] = res
            return memo[i]
        
        return dfs(0)
    
        """
        Optimized:
        1. Pass index instead of days[] list
        2. Calculate next index instead of modifying next days[] list
        
        """

#         def next_index(curr_index, duration): # calculate next day's index
#             j = curr_index
#             while j < len(days) and days[j] < days[curr_index] + duration:
#                 j += 1
#             return j
        
#         @lru_cache(None)
#         def dp(index):
            
#             if index >= len(days):
#                 return 0

#             j = next_index(index, 1)
#             cost_0 = costs[0] + dp(j)

#             j = next_index(index, 7)
#             cost_1 = costs[1] + dp(j)

#             j = next_index(index, 30)
#             cost_2 = costs[2] + dp(j)

#             return min(cost_0, cost_1, cost_2)

#         return dp(0)
        
    
        """
        DP (bottom up)
        
        dp[i+1]: money spent to travel till day i+1
        
        for one (duration, cost) option, i
        
        Time O(3 * days[-1])
        Space O(days[-1])
        
        """
#         s = set(days)
#         covers = [1, 7, 30]
#         dp = [0] + [0] * days[-1]
        
#         for i in range(1, len(dp)):
            
#             if i not in s: # if not a day in days, use value carried on from last valid day
#                 dp[i] = dp[i - 1]

#             else:
#                 dp[i] = min([dp[(i-cover) if i-cover >= 0 else 0] + cost for cover, cost in zip(covers, costs)])
                
#         return dp[-1]
