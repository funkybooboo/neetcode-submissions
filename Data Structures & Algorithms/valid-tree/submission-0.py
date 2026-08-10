from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        if n == 0:
            return True

        # Build adjacency list: u → list of its neighbors
        adj_list: List[List[int]] = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        completed: set[int] = set()   # nodes fully processed (no cycles downstream)
        visiting: set[int] = set()    # nodes in the current DFS recursion stack
        cycle: bool = False           # global flag—set True if we detect a cycle

        def dfs_visit(u: int, parent: int) -> bool:
            nonlocal cycle
            if cycle:
                return False

            # cycle if we see a node already on the recursion stack
            if u in visiting:
                cycle = True
                return False

            # already checked this node and its prerequisites
            if u in completed:
                return True

            visiting.add(u)
            for v in adj_list[u]:
                # Avoid going back to the parent node
                if v != parent:
                    if not dfs_visit(v, u):
                        return False
            visiting.remove(u)

            completed.add(u)
            return True

        # Start DFS from node 0
        if not dfs_visit(0, -1):
            return False

        # Ensure all nodes are visited (i.e., the graph is connected)
        return len(completed) == n
