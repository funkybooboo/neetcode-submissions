from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        if len(intervals) == 1:
            return 1

        start_times: list[int] = sorted([i.start for i in intervals])
        end_times: list[int] = sorted([i.end for i in intervals])

        max_count = count = 0
        start_index = end_index = 0
        while start_index < len(intervals):
            if start_times[start_index] < end_times[end_index]:
                start_index += 1
                count += 1
            else:
                end_index += 1
                count -= 1
            max_count = max(max_count, count)
        return max_count
