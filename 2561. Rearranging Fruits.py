class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        """
        Greedy
        
        - Count net frequency difference of each value between basket1 and basket2
        - If any value has odd difference, equalization is impossible
        - Each surplus element needs to be swapped with a deficit element
        - For each swap, cost is min(value, 2 * global_min),
          because swapping indirectly via the smallest element may be cheaper
        - Sort all required swap values and only pay for half of them (each swap fixes two elements)

        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """

        freq = Counter()
        global_min = float("inf")

        # Count frequencies and track global minimum
        for x in basket1:
            freq[x] += 1
            global_min = min(global_min, x)
        for x in basket2:
            freq[x] -= 1
            global_min = min(global_min, x)

        to_swap = []

        # Build list of elements that need swapping
        for val, diff in freq.items():
            if diff % 2 != 0:
                return -1  # impossible
            to_swap.extend([val] * (abs(diff) // 2))

        if not to_swap:
            return 0

        to_swap.sort()

        # Only need to pay for half (each swap handles two items)
        half = len(to_swap) // 2
        return sum(min(x, 2 * global_min) for x in to_swap[:half])
