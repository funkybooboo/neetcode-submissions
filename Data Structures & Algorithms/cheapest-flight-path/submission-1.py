from collections import defaultdict, deque
from typing import List, Dict, Tuple


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build graph
        adj_list: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
        for u, v, w in flights:
            adj_list[u].append((v, w))

        # BFS queue: (current_city, total_cost, stops_so_far)
        q = deque([(src, 0, 0)])

        # Dict to track the minimum cost to reach (city, stops)
        visited: Dict[Tuple[int, int], int] = {}

        min_cost = float('inf')

        while q:
            city, cost, stops = q.popleft()

            if stops > k + 1:
                continue

            if city == dst:
                min_cost = min(min_cost, cost)
                continue

            for neighbor, price in adj_list[city]:
                new_cost = cost + price
                if new_cost >= min_cost:
                    continue  # Prune more expensive path
                if (neighbor, stops + 1) not in visited or visited[(neighbor, stops + 1)] > new_cost:
                    visited[(neighbor, stops + 1)] = new_cost
                    q.append((neighbor, new_cost, stops + 1))

        return min_cost if min_cost != float('inf') else -1
