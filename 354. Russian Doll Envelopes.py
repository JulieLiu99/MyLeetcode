class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        Longest increasing sequence: Greedy
        
        If new item is larger than all: append to the end
        
        Else, binary search to insert in new item and replace existing item
        - It does not change the length
        - It gives future items more chance to get appended
        
        0, 8, 4, 10, 2, ...
        [0]
        [0, 8]
        [0, 4]
        [0, 4, 10]
        [0, 2, 10]
        ...
        
        Why sort by width, small to big, but sort by hight, big to small? 
        If sort hight small to bit too, we will get duplicates in the list!
        [[4, 5], [4, 6]] WRONG!
        
        Correct example:
        (1, 9) [9]
        (2, 3) [3]
        (2, 2) [2]
        (5, 4) [2, 4]
        (6, 7) [2, 4, 7]
        (6, 4) [2, 4, 7]
        (6, 1) [1, 4, 7]
        (7, 8) [1, 4, 7, 8]
        (7, 6) [1, 4, 6, 8]
        
        Time O(nlogn)
        """
        envelopes.sort(key=lambda x: (x[0], -x[1])) # sort by width, small to big; sort by hight, big to small
        LIS = []
        res = 0
        for (w, h) in envelopes:
            if not LIS or h > LIS[-1]: # a higher one -> append
                LIS.append(h)
                res += 1
            else:                      # a shorter one -> replace within LIS
                i = bisect.bisect_left(LIS, h)
                LIS[i] = h
        return res
    
        
        """
        DP: O(n^2) TLE
        """
#         envelopes.sort()
#         n = len(envelopes)
#         dp = [1] * n # dp[i]: longest increasing sequence till envelopes[i]
        
#         # for each item, compare with all previous items to update dp[i]
#         for i in range(1, n):
#             for j in range(i):
#                 if envelopes[i][1] > envelopes[j][1] and envelopes[i][0] != envelopes[j][0]:
#                     dp[i] = max(dp[i], dp[j]+1)
                    
#         return max(dp)
