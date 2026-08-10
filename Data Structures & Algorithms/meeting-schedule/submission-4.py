"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        
        intervals.sort(key=lambda x: x.start)

        prev_interval = intervals[0]
        for interval in intervals[1:]:
            if prev_interval.end > interval.start:
                return False
            prev_interval = interval

        return True

