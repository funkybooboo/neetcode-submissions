from collections import defaultdict, deque
from typing import List, Dict, Tuple


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Adjacency list
        adj_list: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
        for u, v, w in flights:
            adj_list[u].append((v, w))

        # Queue: (current_city, current_cost, stops_used)
        q = deque([(src, 0, 0)])

        # Dictionary to record the minimum cost to reach a city with certain stops
        visited = dict()

        min_cost = float('inf')

        while q:
            city, cost, stops = q.popleft()

            # If we exceed allowed stops, skip
            if stops > k + 1:
                continue

            # If we reached destination, record the cost
            if city == dst:
                min_cost = min(min_cost, cost)
                continue

            # If we have visited this city with fewer or equal stops and less cost, skip
            if (city in visited and visited[city] <= stops):
                continue

            visited[city] = stops

            for neighbor, price in adj_list[city]:
                if cost + price >= min_cost:
                    continue  # Prune more expensive paths
                q.append((neighbor, cost + price, stops + 1))

        return min_cost if min_cost != float('inf') else -1
