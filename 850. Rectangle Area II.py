class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        
        """
        
        Time O(n^2 logn): Scan through x. For each x, calculate Area and sort new y intervals O(n + nlogn) = O(nlogn)
        Space O(n)
        
        """

        def getArea(width):
            height = 0
            bottom, top = 0, 0
            for y1, y2 in y_intervals:
                # if intersect, update range
                if y1<=top and bottom<=y2:
                    bottom = min(bottom, y1)
                    top = max(top, y2)
                # else add range to height, start new range
                else:
                    height += (top-bottom)
                    bottom = y1
                    top = y2
            # add the last range
            height += (top-bottom)
            return height*width
        
        
        MOD = 10**9 + 7
        events = []
        
        for x1, y1, x2, y2 in rectangles:
            events.append((x1, 0, y1, y2))  # start
            events.append((x2, 1, y1, y2))  # end
            
        events.sort(key=lambda x:(x[0], x[1])) # sort x ASC, starts before ends
        y_intervals = []
        
        ans = 0
        prev_x = 0
        # for each x intervals/ width, find the heights
        for cur_x, end, y1, y2 in events:
            ans += getArea(cur_x - prev_x)
            
            if end:
                y_intervals.remove((y1, y2))
            else:
                # add starting height for the next area
                y_intervals.append((y1, y2))
                y_intervals.sort()
                
            prev_x = cur_x
                
        return ans % MOD
