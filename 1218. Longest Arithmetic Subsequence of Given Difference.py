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
        
        
        Time O(n)
        Space O(n)
        
        """
        sub_length = {}
        res = float('-inf')
        for num in arr:
            if num - difference in sub_length: # (num - difference) is last num in subsequnce
                sub_length[num] = sub_length[num - difference] + 1
            else:
                sub_length[num] = 1

            res = max(res, sub_length[num])

        return res
