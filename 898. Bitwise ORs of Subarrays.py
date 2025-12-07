class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        """
        One pass of array
        Track distinct OR results of subarrays
        At each new num, OR it with the prev results
        Avoids recomputing ORs of prev subarrays

        Time O(nB), where B is number of bits (≤ 30), effectively O(n). 
        As we OR numbers, bits only change from 0 to 1, and never back to 0 
        -> OR values can increase only B times before they stop changing 
        -> prev never grows beyond ~30 numbers
        
        Space O(B) ≈ O(1)
        """
        all_or_values = set()
        prev_or_values = set()
        
        for num in arr:
            current_or_values = {num}
            for prev in prev_or_values:
                current_or_values.add(prev | num)

            all_or_values.update(current_or_values)
            prev_or_values = current_or_values
        
        return len(all_or_values)
