class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        """
        Track counts of moves in each direction
        Compute the raw Manhattan distance (MD)

        Example:
        N, N, S -> steps= 3, MD = 1
        (steps - MD) measures cancellation

        Time O(n)
        Space O(1)
        """
        max_distance = 0
        north = south = east = west = 0
        
        for i in range(len(s)):
            c = s[i]
            if c == 'N':
                north += 1
            elif c == 'S':
                south += 1
            elif c == 'E':
                east += 1
            elif c == 'W':
                west += 1
            
            x = abs(north - south)
            y = abs(east - west)
            MD = x + y

            steps = i + 1

            # 2 * k: each edit can increase distance by at most 2
            # steps - MD: max possible extra distance without cancellation
            extra_gain = min(2 * k, steps - MD)

            distance = MD + extra_gain
            max_distance = max(max_distance, distance)
        
        return max_distance
