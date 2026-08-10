from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency = [[] for _ in range(n)]
        for u, v in edges:
            adjacency[u].append(v)
            adjacency[v].append(u)

        visited = [False] * n

        def dfs(u: int):
            for v in adjacency[u]:
                if not visited[v]:
                    visited[v] = True
                    dfs(v)

        components = 0
        for u in range(n):
            if not visited[u]:
                visited[u] = True
                dfs(u)
                components += 1

        return components
