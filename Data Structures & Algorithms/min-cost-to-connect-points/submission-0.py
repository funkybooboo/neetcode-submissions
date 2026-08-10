from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0

        def dist(i: int, j: int) -> int:
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        in_mst  = [False] * n
        best_to = [float('inf')] * n
        best_to[0] = 0

        total = 0
        for _ in range(n):
            # pick the unseen vertex with the smallest connecting edge
            u = -1
            best = float('inf')
            for i in range(n):
                if not in_mst[i] and best_to[i] < best:
                    best, u = best_to[i], i

            in_mst[u] = True
            total += best

            # update distances using the new vertex u
            for v in range(n):
                if not in_mst[v]:
                    d = dist(u, v)
                    if d < best_to[v]:
                        best_to[v] = d

        return total
