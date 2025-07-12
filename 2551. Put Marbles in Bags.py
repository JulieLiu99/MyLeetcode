class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # score = first val + sum(val of splits) + last val
        # where val of split = val_prev + val_next
        # [1,3,5,1]
        #  ^     ^      first + last
        #    ^|^         prev + next
        # Get values of all possible splits
        # Sort them for max and min scores
        # Time O(nlogn)
        # Space O(n)
        if k == 1:
            return 0

        splits = []
        for i in range(len(weights) - 1):
            splits.append(weights[i]  + weights[i+1])

        splits.sort()

        n_splits = k - 1

        max_score = weights[0] + weights[-1] + sum(splits[-n_splits:])
        min_score = weights[0] + weights[-1] + sum(splits[:n_splits])

        return max_score - min_score
