class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Min Heap of meeting rooms and their end times
        Whenever there is an overlapping meeting, add another room

        Time O(nlogn)
        Space O(n)
        """
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0]) # sort meetings by start time

        min_heap = [intervals[0][1]] # end time of the first meeting

        for interval in intervals[1:]:

            # non-overlapping meeting, extend end time of the room
            if interval[0] >= min_heap[0]: 
                heapq.heappop(min_heap)
            
            heapq.heappush(min_heap, interval[1])

        return len(min_heap)