import collections
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build the graph as an adjacency list
        graph = collections.defaultdict(list)
        for source, target, weight in times:
            graph[source].append((target, weight))

        # Min-heap to always process the closest unvisited node
        min_heap = [(0, k)]  # (current_time, current_node)
        visited = set()
        max_time = 0

        while min_heap:
            current_time, node = heapq.heappop(min_heap)

            if node in visited:
                continue

            visited.add(node)
            max_time = current_time  # Update the latest time reached

            # Add all neighbors to the heap
            for neighbor, travel_time in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (current_time + travel_time, neighbor))

        # If all nodes are visited, return the time it took; otherwise, return -1
        return max_time if len(visited) == n else -1
