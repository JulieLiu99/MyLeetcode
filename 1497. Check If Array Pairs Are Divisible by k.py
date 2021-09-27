class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        remainder_count = collections.defaultdict(int)
        for a in arr:
            remainder_count[a%k] += 1

        for remainder in range(k):
            if remainder == 0:
                if remainder_count[remainder] % 2 != 0: # can't form a pair
                    return False
            elif remainder_count[remainder] != remainder_count[k-remainder]:
                return False

        return True
