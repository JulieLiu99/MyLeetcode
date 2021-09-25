class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        """
        Two Pointers
        If next arr[r+1] - arr[r] == difference: r += 1
        Else: l = r+1, r = l + 1
        Record max length seen so far
        ^
        Cannot use this because subsequence doesn't have to be continuous
        
        Has to use DP
        where dp[num] = length of subsequence seen so far (that ends with num)
        
        For each new number in array, check if it can be appended to an existing subsequence
        If yes, dp[num] = dp[last num of existing subsequence] + 1
        If no, start a new subsequence dp[num] = 1
        
        Time O(n)
        Space O(n)
        
        """
        dp = {}
        for num in arr:
            if num - difference in dp: # (num - difference) is last num in subsequnce
                dp[num] = dp[num - difference] + 1
            else:
                dp[num] = 1

        return max(dp.values())