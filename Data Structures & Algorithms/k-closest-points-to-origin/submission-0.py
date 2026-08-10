from math import sqrt
from typing import List, Tuple
import heapq

ORIGIN_X = 0
ORIGIN_Y = 0

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Compute Euclidean distance from origin
        def euclidean_distance(point: List[int]) -> float:
            x, y = point
            dx = x - ORIGIN_X
            dy = y - ORIGIN_Y
            return sqrt(dx * dx + dy * dy)

        # Each heap entry is (distance, point). The heap is sorted by the first item (distance).
        distance_heap: List[Tuple[float, List[int]]] = [
            (euclidean_distance(point), point) for point in points
        ]

        heapq.heapify(distance_heap)

        # Pop k closest points (smallest distances)
        return [heapq.heappop(distance_heap)[1] for _ in range(k)]
