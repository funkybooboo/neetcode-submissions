from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._k = k
        self._heap = nums
        heapq.heapify(self._heap)
        while len(self._heap) > k:
            heapq.heappop(self._heap)  # keep only k largest

    def add(self, val: int) -> int:
        if len(self._heap) < self._k:
            heapq.heappush(self._heap, val)
        elif val > self._heap[0]:
            heapq.heapreplace(self._heap, val)  # faster than heappop+heappush
        return self._heap[0]
