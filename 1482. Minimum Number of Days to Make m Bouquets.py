class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        """
        Binary search
        
        Time O(log(max(bloomDay) * N)
        Space O(1)
        
        """
        
        def isOK(day, bloomDay, m, k):
            counter = bouq = 0
            for day in bloomDay:
                counter = 0 if day > mid else counter + 1
                if counter >= k:
                    counter = 0
                    bouq += 1
                    if bouq == m: 
                        return True
            return False
                        
        
        if m * k > len(bloomDay): return -1
        
        left, right = 1, max(bloomDay)
        
        while left < right:
            mid = left + (right-left) // 2
                        
            if isOK(mid, bloomDay, m, k):
                right = mid
            else:
                left = mid + 1
                
        return left
