from copy import deepcopy
from typing import List, Optional


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals: List[List[int]] = deepcopy(intervals)

        sorted_intervals.sort(key=lambda x: x[0])

        merged_intervals: List[List[int]] = []
        current_merge: List[int] = []
        for interval in sorted_intervals:
            if not current_merge:
                current_merge = interval
                continue

            if current_merge[1] >= interval[0]:
                current_merge[0] = min(current_merge[0], interval[0])
                current_merge[1] = max(current_merge[1], interval[1])
                continue

            merged_intervals.append(current_merge)
            current_merge = interval

        merged_intervals.append(current_merge)

        return merged_intervals
