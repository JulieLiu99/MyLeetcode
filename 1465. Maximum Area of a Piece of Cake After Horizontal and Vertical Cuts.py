class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        # Intuition: max area = max width * max height
        # Time: O(nlogn)
        # Space: O(n)
        
        def maxDistance(cuts, bound):
            cuts.sort()
            maxDist = cuts[0] # 0 to first cut
            for i in range(len(cuts) - 1):
                maxDist = max(maxDist, cuts[i+1] - cuts[i]) # between this cut and next cut
            maxDist = max(maxDist, bound - cuts[-1]) # last cut to bound
            return maxDist

        return (maxDistance(horizontalCuts, h) * maxDistance(verticalCuts, w)) % (10**9 + 7)
