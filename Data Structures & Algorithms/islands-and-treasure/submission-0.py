from collections import deque
from typing import List, Set, Tuple

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Mutate `grid` in-place so that every land cell (INF = 2147483647)
        is replaced by the shortest distance to any treasure (0). Water cells
        (-1) remain unchanged. Traversal is allowed up/down/left/right only.
        """
        if not grid or not grid[0]:
            return

        rows = len(grid)
        cols = len(grid[0])

        visited: Set[Tuple[int, int]] = set()
        queue: deque[Tuple[int, int]] = deque()

        # Enqueue all treasure cells (value == 0)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        def enqueue_if_valid(r: int, c: int) -> None:
            """
            Enqueue the cell (r, c) if:
              - it’s inside the grid bounds
              - it’s not been visited yet
              - it’s not an obstacle (-1)
            """
            if (
                0 <= r < rows
                and 0 <= c < cols
                and (r, c) not in visited
                and grid[r][c] != -1
            ):
                visited.add((r, c))
                queue.append((r, c))

        distance = 0
        # Perform BFS layer by layer
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = distance
                enqueue_if_valid(r + 1, c)
                enqueue_if_valid(r - 1, c)
                enqueue_if_valid(r, c + 1)
                enqueue_if_valid(r, c - 1)
            distance += 1
