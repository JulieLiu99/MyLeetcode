class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        """
        https://www.youtube.com/watch?v=g5wLHFTodm0
        
        Min-Max Strategy
        Resursion + Memorization
        
        Time O(N^2): look at O(N^2) cases, each recursion taking O(1) time bc memorization
        Space O(N^2 + N)
        
        """
        dp = {}

        def find(l, r):
            if (l, r) not in dp:
                if l == r:  # at leaf node
                    return nums[l]
                dp[l,r] = max(nums[l]-find(l+1, r), 
                              nums[r]-find(l, r-1))
            return dp[l,r]

        return find(0, len(nums)-1) >= 0
