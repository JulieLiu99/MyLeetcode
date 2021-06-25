class Solution:
    def trap(self, height: List[int]) -> int:
        
        """

        For column_i, the rain it can trap:
        r[i] = min(max(h[0~i]), max(h[i~n-1])) - h[i]

        ans = sum(r[i])

        -----------------------
        Approach 1: Brute Force

        For each column, 
        search left and right, find max of both sides which takes O(n)

        Time O(n^2)
        Space O(1)

        --------------------------
        Approach 2: DP, prefix max

        Pre-compute the max of h[0~i] and h[i~n-1] in O(n)

        l[i] := max(h[0~i])
        r[i] := max(h[i~n-1])

        l[i] = max(h[i], l[i-1])   i: 0 ~ n-1
        r[i] = max(h[i], r[i+1])   i: n-1 ~ 0

        For each column, query the max is reduced to O(1)
        Time O(n)
        Space O(n)

        ------------------------
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
        n = len(height) 
        if n == 0: return 0
        
        l = 0
        r = n - 1
        max_l = height[l]
        max_r = height[r]
        ans = 0

        while l < r:
            if max_l < max_r:
                ans += max_l - height[l]
                l += 1
                max_l = max(max_l, height[l])
            else:
                ans += max_r - height[r]
                r -= 1
                max_r = max(max_r, height[r])

        return ans
