from collections import defaultdict
from heapq import heappush, heappop
from typing import List, Dict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        Reconstruct the itinerary starting from 'JFK' using all tickets exactly once.
        When multiple choices exist, choose the lexicographically smallest next airport.

        Strategy: Hierholzer’s algorithm for Eulerian path with lexical tie-breaking.
        We store destinations in min-heaps to always grab the smallest next hop.
        """
        # Build graph: origin -> min-heap of destinations
        graph: Dict[str, List[str]] = defaultdict(list)
        for src, dst in tickets:
            heappush(graph[src], dst)

        route: List[str] = []   # will hold the itinerary in reverse
        stack: List[str] = ["JFK"]

        # Iterative Hierholzer: walk until you hit a node with no outgoing edges,
        # then add it to the route; otherwise, keep following the smallest edge.
        while stack:
            curr = stack[-1]
            if graph[curr]:
                next_stop = heappop(graph[curr])
                stack.append(next_stop)
            else:
                route.append(stack.pop())

        return route[::-1]
