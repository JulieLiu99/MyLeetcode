
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Brute Force: 
        Try every single starting point, go through the lists from there
        
        Time O(n^2)
        Space O(n)
        
        """
#         res = -1
        
#         def canComplete(i):
#             gass = gas[i:] + gas[:i]
#             costt = cost[i:] + cost[:i]
#             cur = 0
#             for i in range(len(gass)):
#                 cur += gass[i]
#                 cur -= costt[i]
#                 if cur < 0:
#                     return False
                
#             return True
        
#         for i in range(len(gas)):
#             if canComplete(i):
#                 res = i
        
#         return res

        """
        Space Optimization:
        Instead of creating new lists with idx as starting point
        Go through the list idx -> len(list)-1, 0 -> idx-1
        
        Time Optimization:
        Since if there exists a solution, it is guaranteed to be unique,
        Stop trying new starting point when canComplete returns True
        
        Time O(n^2)
        Space O(1)
        
        """
    
#         res = -1
        
#         def canComplete(idx):
#             cur = 0
#             for i in range(idx, len(gas)):
#                 cur += gas[i]
#                 cur -= cost[i]
#                 if cur < 0:
#                     return False
#             for i in range(idx):
#                 cur += gas[i]
#                 cur -= cost[i]
#                 if cur < 0:
#                     return False
                
#             return True
        
#         for i in range(len(gas)):
#             if canComplete(i):
#                 res = i
#                 break
        
#         return res
            
        """
        Keep track of gas_tank
        Go through indexes only once
        
        If gas_tank goes to negative,
        Try the next index as start_index.
        Because none of the indexes from original start_index to current index has enough gas to be start_index.
        At current index for example, you have at least gas[current index] to go, plus non-negative gas from before, but still not enough to move forward --> cannot be start_index.
        Same logic for all previous indexes.
        
        Time O(n)
        Space O(1)
        
        """

        if (sum(gas) - sum(cost) < 0):
            return -1
        
        gas_tank = 0
        start_index = 0
        
        for i in range(len(gas)):
            gas_tank += gas[i] - cost[i]
            
            if gas_tank < 0:
                start_index = i+1
                gas_tank = 0
            
        return start_index
