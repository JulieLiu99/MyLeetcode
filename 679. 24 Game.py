class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        """
        Backtracking

        DFS over all ways to pick two numbers
        Combine them using + - * /
        Repeat until one number remains and check if it is 24

        Time: O(n!(n-1)! * 3^(n-1))
        - levels k=n..2: pick a pair in C(k,2) -> ∏C(k,2) = n!(n-1)! / 2^(n-1)
        - for each pair try <= 6 ops, so overall ∏C(k,2) * 6^(n-1)

        Space: O(n) recursion depth ≤ n
        """
        # epsilon: tolerance for float comparison
        # compensates floating-point rounding error from divisions
        EPS = 1e-6

        def dfs(nums: List[float]) -> bool:
            # base case: if only one num left, check if equals 24
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPS # nums[0] == 24

            n = len(nums)
            # recurrence: pick two numbers, combine them
            for i in range(n):
                for j in range(i+1, n):
                    a, b = nums[i], nums[j]
                    rest = nums[:i] + nums[i+1:j] + nums[j+1:]  # remaining numbers

                    # all results from combining a and b
                    candidates = [a+b, a-b, b-a, a*b]
                    if a:
                        candidates.append(b/a)
                    if b:
                        candidates.append(a/b)

                    for val in candidates:
                        if dfs(rest + [val]):  # recurse with one fewer number
                            return True
            return False

        return dfs([float(card) for card in cards])
