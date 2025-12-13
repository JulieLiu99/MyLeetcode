class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        """
        Sliding window
        Track max sum of gaps = max free time possible

        Time O(n)
        Space O(n)
        """
        n = len(startTime)
        gaps = [0] * (n + 1) # n + 1 gaps in total
        gaps[0] = startTime[0] # gap before the first meeting

        # gaps between meetings
        for i in range(1, n):
            gaps[i] = startTime[i] - endTime[i - 1]

        gaps[n] = eventTime - endTime[n - 1] # gap after the last meeting

        window_size = k + 1 # k + 1 adjacent gaps
        window_sum = sum(gaps[:window_size])
        max_free_time = window_sum

        for i in range(window_size, n + 1):
            window_sum += gaps[i]
            window_sum -= gaps[i - window_size]
            max_free_time = max(max_free_time, window_sum)

        return max_free_time
