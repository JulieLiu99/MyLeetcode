class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        """
        
        1. Get the first and last occurance of each characters
        2. For the range of each letter, update the range according to all the characters within the range. 
        E.g. "abab" has initial range a: [0,2], b: [1:3]. Since the range of a [0,2] includes b, we need to update the range of a to also include all occurances of b as well.
        3. Sort all the ranges according to their ends. Take as many ranges as we can, as long as the start of the current range is >= the end of the previous range.

        Time O(N)
        
        1) Loop through s once, so O(N) where N is the length of s
        2) Loop through all ranges, and there could be at most 26 ranges so O(26). Depending on how many other characters included in each range, we would be spending another 26 loops within the loop, so total O(26*26)
        3) Loop through all the ranges generated from #2, so it's O(26*26). We also spent O(26*26log(26*26)) to sort it.
        
        Space O(26) to store (start, end) for each char, and O(26*26) to store pairs:[l, r].
        
        """
          
        # Step 1: find the (start, end) positions for each character
        
        # This works faster though theoretically time complexity worse
        # start_end = {c: [s.index(c), s.rindex(c)+1] for c in set(s)}
        # The index() method has linear runtime complexity in the number of list elements. 
        
        start_end = collections.defaultdict(list)
        for i, char in enumerate(s): 
            if char not in start_end: 
                start_end[char] = [i, i+1]   # update (start, end) position
            else: 
                start_end[char][1] = i+1     # update end position 
        
        # input string has only one unique char
        if len(start_end) == 1: return [s]
        
        # Step 2: 
        # find all the correct boundries
        pairs = []
        for char in set(s):
            l = tmpl = start_end[char][0]
            r = tmpr = start_end[char][1]
            while True:
                # set(): convert any of the iterable to sequence of iterable elements with distinct elements
                interval = set(s[tmpl:tmpr])
                for ic in interval:
                    tmpl = min(tmpl, start_end[ic][0])
                    tmpr = max(tmpr, start_end[ic][1])
                if (tmpl, tmpr) == (l, r):
                    break
                l, r = tmpl, tmpr
            pairs.append([l, r])

        # Step 3: 
        # greedily find the optimal solution
        pairs.sort(key=lambda x: x[1])
        res = []
        prev_r = 0
        for l, r in pairs:
            if l >= prev_r:
                res.append(s[l:r])
                prev_r = r
        return res
