from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0

        intervals.sort(key=lambda x: x[0])

        count = 0
        previous_interval = intervals[0]
        for interval in intervals[1:]:
            if interval[0] < previous_interval[1]:
                count += 1
                if interval[1] < previous_interval[1]:
                    previous_interval = interval
            else:
                previous_interval = interval

        return count
