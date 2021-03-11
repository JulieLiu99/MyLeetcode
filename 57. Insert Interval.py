class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        """
        Time O(n): linear traversal through the existing intervals
        Space O(n): storing each existing interval once
        
        """
        
        new_start, new_end = newInterval[0], newInterval[1]
        left, right = [], []
        
        for inter in intervals:
            
            if inter[1] < new_start:
                left.append(inter),
                
            elif inter[0] > new_end:
                right.append(inter),
                
            else:
                new_start = min(new_start, inter[0])
                new_end = max(new_end, inter[1])
                
        return left + [[new_start, new_end]] + right
