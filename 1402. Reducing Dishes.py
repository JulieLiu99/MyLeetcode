class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """
        1. Sort by satisfaction in descending order
        2. Track marginal benefit to cook current dish + prev dishes once more, the "runningSum"
        3. If positive margin, add to result 

        Time O(NlogN)
        Space O(1)
        
        """
        satisfaction.sort(reverse=True)
        
        runningSum = 0
        result = 0
        
        for val in satisfaction:
            runningSum += val
			# if no longer beneficial to serve the next dish
            if runningSum < 0:
                break
            result += runningSum
        
        return result
