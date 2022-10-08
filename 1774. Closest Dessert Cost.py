class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        """
        DFS
        
        Time O(n * 3^m): O(n) for base and O(3^m) for toppings as each has three possibilities (0,1,2)
        Space O(3^m): 3-way recursive stack
        
        """
        
        res = diff = float('inf')
        
        n = len(baseCosts)
        m = len(toppingCosts)
        
        
        def backtrack(cost, target, i):
            nonlocal res, diff
            
            if abs(cost - target) < diff:
                diff = abs(cost - target)
                res = cost
            elif abs(cost - target) == diff: # if there are multiple, return the lower one
                res = min(res, cost)
            
            if i == m: # tried all toppings
                return
            
            for count in [0, 1, 2]: # try next topping, at most two of it
                backtrack(cost + toppingCosts[i] * count, target , i+1)
        
        for baseCost in baseCosts:
            backtrack(baseCost, target, 0)
            
        return res
