from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)  # Number of edges; since the graph was originally a tree, n is also the number of nodes
        if n == 0:
            return []

        # Create an adjacency list to represent the undirected graph.
        # Node labels are 1-based, so we use size (n + 1) to safely index from 1 to n.
        adj_list = [[] for _ in range(n + 1)]

        # Depth-First Search to determine if a path exists between `u` and `target`.
        def dfs(u: int, target: int, visited: List[bool]) -> bool:
            if u == target:
                return True  # Found a path to the target node
            visited[u] = True  # Mark the current node as visited
            for neighbor in adj_list[u]:
                if not visited[neighbor]:
                    if dfs(neighbor, target, visited):
                        return True  # Found path through neighbor
            return False  # No path found from this branch

        # Iterate through each edge in the graph
        for u, v in edges:
            visited = [False] * (n + 1)  # Reset visited before each DFS call

            # Check if there's already a path between `u` and `v`
            # If yes, adding this edge would create a cycle
            if dfs(u, v, visited):
                return [u, v]  # This edge introduces a cycle — it's redundant

            # If no cycle found, add the edge to the graph
            adj_list[u].append(v)
            adj_list[v].append(u)

        return []  # Fallback — problem guarantees there's one redundant edge, so this won't be reached
