from typing import List, Set, Tuple

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])

        # Four possible directions: down, up, right, left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r: int, c: int, visited: Set[Tuple[int, int]], prev_height: int) -> None:
            # Boundary checks and monotonicity check
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                (r, c) in visited or
                heights[r][c] < prev_height
            ):
                return

            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        pacific_reachable: Set[Tuple[int, int]] = set()
        atlantic_reachable: Set[Tuple[int, int]] = set()

        # Start DFS from all Pacific-bordering cells (top row and left col)
        for c in range(cols):
            dfs(0, c, pacific_reachable, heights[0][c])
        for r in range(rows):
            dfs(r, 0, pacific_reachable, heights[r][0])

        # Start DFS from all Atlantic-bordering cells (bottom row and right col)
        for c in range(cols):
            dfs(rows - 1, c, atlantic_reachable, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, cols - 1, atlantic_reachable, heights[r][cols - 1])

        # Collect cells reachable by both oceans
        result: List[List[int]] = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    result.append([r, c])

        return result