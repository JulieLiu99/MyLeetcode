class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        """
        Convert both to percentage:
        hour/12
        minutes/60
        
        Note: 
        1. hour's percentage/angle isn't just itself, has to add minutes/60 first!!!
        2. hour might go over 12, so %12 first !!!
        
        Computer angles from both directions -> return smaller one
        
        Time O(1)
        Space O(1)
        """
        minutes /= 60
        hour = (hour%12 + minutes) / 12
        
        # from percentage to degrees
        minutes *= 360
        hour *= 360
        
        # make minutes the bigger one
        if minutes < hour:
            minutes, hour = hour, minutes

        # either clock-wise or counter-clock-wise angle
        return min(minutes-hour, 360-minutes+hour)
