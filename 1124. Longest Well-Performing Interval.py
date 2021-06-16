class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        """
        Presum
        
        h = [9, 9, 6, 0, 6, 6, 9]
        v = [+1,+1,-1,-1,-1,-1,+1]
        
        score(v[0:i]) = v[0] + ... + v[i]
        Reduce the problem to find target_sum = 1
        if score(v[0:n]) > 0, return n
        
        Use a hashtable to store the first index of the cumulative sum
        ans = max{i - index[score-1]}

        Time O(N) for one pass.
        Space O(N) in worst case if no tiring day.
        
        """
        length = 0
        score = 0
        index = {}
        
        for i, h in enumerate(hours):
            
            score = score + 1 if h > 8 else score - 1
            
            if score > 0:
                length = i + 1
                
            if not score in index: 
                index[score] = i
                
            if score - 1 in index:
                length = max(length, i - index[score - 1])
                
        return length
