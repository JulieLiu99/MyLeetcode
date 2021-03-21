class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
     
        """
        Use a vertical line to scan from left to right. 
        
        Time O(nlogn): every node addition or removal takes O(logn) time
        Space O(n)
        
        """
        
        """
        # Leetcode doesn't have SortedList
        
        events = []
        for l, r, h in buildings:
            events.append((l, h, 1))
            events.append((r, h, 0))
            
        events.sort()
        
        ans = []
        active_heights = SortedList([0])
        n = len(events)
        i = 0
        while i < n:
            cur_x = events[i][0]
            
            # process all events with same x together
            while i < n and events[i][0] == cur_x:
                x, h, start = events[i]
                
                if start:   
                    active_heights.add(h)
                else:
                    active_heights.remove(h)
                    
                i += 1
            
            # check if the biggest height has changed
            if not ans or ans[-1][1] != active_heights[-1]:
                ans.append((cur_x, active_heights[-1]))
                
        return ans
        """
        
        
        # Change to min heap instead
        # use -H so that it pops out the max
        # 不难发现这些关键点的特征是：竖直线上轮廓升高或者降低的终点
        # 所以核心思路是：从左至右遍历建筑物，记录当前的最高轮廓，如果产生变化则记录一个关键点
        
        # 首先记录构造一个建筑物的两种关键事件
        # 第一种是轮廓升高事件(L, -H)、第二种是轮廓降低事件(R, 0)
        # 轮廓升高事件(L, -H, R)中的R用于后面的最小堆
        events = [(L, -H, R) for L, R, H in buildings]
        events += list({(R, 0, 0) for _, R, _ in buildings})

        # 先根据L从小到大排序、再根据H从大到小排序(记录为-H的原因)
        # 这是因为我们要维护一个堆保存当前最高的轮廓
        events.sort()

        # 保存返回结果
        res = [[0, 0]]
        
        # 最小堆，保存当前最高的轮廓(-H, R)，用-H转换为最大堆，R的作用是记录该轮廓的有效长度
        live = [(0, float("inf"))]

        # 从左至右遍历关键事件
        for L, negH, R in events:
            
            # 如果是轮廓升高事件，记录到最小堆中
            if negH: heappush(live, (negH, R))
            
            # 获取当前最高轮廓
            # 根据当前遍历的位置L，判断最高轮廓是否有效
            # 如果无效则剔除，让次高的轮廓浮到堆顶，继续判断
            while live[0][1] <= L: 
                heappop(live)
            
            # 如果当前的最高轮廓发生了变化，则记录一个关键点
            if res[-1][1] != -live[0][0]:
                res += [ [L, -live[0][0]] ]
        return res[1:]
