class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        """
        Binary Search 
        
        count(d) counts the number of balls can be placed in to baskets, under the condition that the minimum distance between any two balls is d.

        We want to find the maximum d such that count(d) == m.

        If the count(d) > m , we have too many balls placed, so d is too small.
        If the count(d) < m , we don't have enough balls placed, so d is too large.
        Since count(d) is monotonically decreasing with respect to d, we can use binary search to find the optimal d.
        
        Time O(Nlog(10^9)) or O(NlogM), where M = max(position) - min(position)
        Space O(1)
        
        """
        
        n = len(position)
        position.sort()
        
        def count(d):
            ans, curr = 1, position[0]
            for i in range(1, n):
                if position[i] - curr >= d:
                    ans += 1
                    curr = position[i]
            return ans
        
        l = 0
        r = position[-1] - position[0]
        while l < r:
            mid = r - (r - l) // 2
            if count(mid) >= m:
                l = mid
            else:
                r = mid - 1
        return l
