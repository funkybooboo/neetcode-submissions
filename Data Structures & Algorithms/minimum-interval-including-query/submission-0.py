from typing import List, Dict


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        if not queries or not intervals:
            return []

        def size_of(start: int, end: int) -> int:
            return end - start + 1

        # { number: smallest size of interval that has that number }
        d: Dict[int, int] = {}
        for interval in intervals:
            start: int = interval[0]
            end: int = interval[1]
            size: int = size_of(start, end)
            for n in range(start, end + 1):
                if n in d:
                    d[n] = min(d[n], size)
                else:
                    d[n] = size

        result: List[int] = []
        for query in queries:
            if query in d:
                result.append(d[query])
            else:
                result.append(-1)

        return result
