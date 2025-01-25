class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Sorting & Two Pointers
        # Convert time to minutes since 00:00
        # Short the minutes
        # Calculate the minimum difference between consecutive times
        # Time O(nlogn) Space O(n)

        def timeToMinutes(time: str) -> int:
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes
        
        minutes = [timeToMinutes(time) for time in timePoints]
        minutes.sort()
        min_diff = float('inf')
        
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
        
        # difference between the last and first time points
        circular_diff = 24*60 - minutes[-1] + minutes[0]
        min_diff = min(min_diff, circular_diff)
        
        return min_diff
