class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        """
        Binary search
        
        Time O(log(sum(weights) - max(weights)) * n)
        Space O(1)
        
        """
        
        def isOK(capacity):
            total, days = 0, 1
            for w in weights:
                if total + w > capacity:
                    days += 1
                    total = w
                else:
                    total += w
            if days <= D:
                return True
            return False
        
        left, right = max(weights), sum(weights)   
        while left < right:
            mid = (left + right) // 2
            if isOK(mid):
                right = mid
            else:
                left = mid+1
        return left
