class Solution:
    def trap(self, height: List[int]) -> int:
        
        """
        For column_i, the rain it can trap:
        r[i] = min(max(h[0~i]), max(h[i~n-1])) - h[i]

        ans = sum(r[i])
        
        Approach 1: Brute Force

        For each column, 
        search left and right, find max of both sides which takes O(n)

        Time O(n^2)
        Space O(1)

        """
        """
        Approach 2: DP, prefix max

        Pre-compute the max of h[0~i] and h[i~n-1] in O(n)

        l[i] := max(h[0~i])
        r[i] := max(h[i~n-1])

        l[i] = max(h[i], l[i-1])   i: 0 ~ n-1
        r[i] = max(h[i], r[i+1])   i: n-1 ~ 0

        For each column, query the max is reduced to O(1)
        Time O(n)
        Space O(n)
        
        """
#         n = len(height) 
#         if n == 0: return 0
        
#         l = [height[0]] + [0] * (n-1)
#         r = [0] * (n-1) + [height[n-1]]
#         ans = 0
        
#         # record max_l for each index 1...n-1
#         for i in range(1, n):
#             l[i] = max(l[i-1], height[i])
            
#         # record max_r for each index n-2...0
#         for i in range(n-2, -1, -1):
#             r[i] = max(r[i+1], height[i])

#         # collect water
#         for i in range(n):
#             ans += min(l[i], r[i]) - height[i]
            
#         return ans
    
        """
        Approach 3: Two pointers

        Use two variables to track the max_l and max_r so far.

        Use l, r to track indexes on two sides
        Move the lower end to the middle and add the water collected so far

        while l < r:
            if max_l < max_r:
                ans += max_l - h[l]
                max_l = max(max_l, h[++l])
            else:
                ans += max_r - h[r]
                max_r = max(max_r, h[--r])

        Time O(n)
        Space O(1)

        """
#         n = len(height) 
#         if n == 0: return 0
        
#         l = 0
#         r = n - 1
#         max_l = height[l]
#         max_r = height[r]
#         ans = 0

#         while l < r:
#             if max_l < max_r:
#                 ans += max_l - height[l]
#                 l += 1
#                 max_l = max(max_l, height[l])
#             else:
#                 ans += max_r - height[r]
#                 r -= 1
#                 max_r = max(max_r, height[r])

#         return ans

        """
        Easier to understand
        
        First pass find peak
        Approach peak from two sides, and collect water
        
        Time O(n)
        Space O(1)
        
        """

        res = 0
        peak = 0
        last_peak_index = 0
        
        for i, h in enumerate(height):
            if h >= peak:
                peak = h
                last_peak_index = i
        
        left_max = 0
        for i in range(0, last_peak_index):
            left_max = max(left_max, height[i])
            res += left_max - height[i]
        
        right_max = 0
        for j in range(len(height)-1, last_peak_index, -1):
            right_max = max(right_max, height[j])
            res += right_max - height[j]
        
        return res