class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        """
        DFS
        
        Time O(n^2)
        """
        @lru_cache(None)
        def dfs(i, target_a, target_b):
            if target_a == 0 and target_b == 0: # complete assignment 
                return 0
            
            if target_a < 0 or target_b < 0: # illegal
                return float('inf')

            # assign to a, or assign to b
            return min(dfs(i+1, target_a-1, target_b) + costs[i][0], \
                       dfs(i+1, target_a, target_b-1) + costs[i][1])    
    
        return dfs(0, len(costs)//2, len(costs)//2)
        
        """
        Sort + Greedy
        The n people who incur the least cost of flying to city B instead of A will be flied to city B
        
        Time O(nlogn)
        """
#         costs.sort(key=lambda x: x[1]-x[0]) # least cost to fly to B instead of A -> most
        
#         n = len(costs)//2 
#         countB = 0
#         res = 0
        
#         while costs:
#             cost = costs.pop()
#             if countB < n:
#                 res += cost[0]
#                 countB += 1
#             else:
#                 res += cost[1]
#         return res
    
