from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        directions = [
            (1, 0),  # down
            (-1, 0),  # up
            (0, 1),  # right
            (0, -1),  # left
        ]
        max_area = 0
        current_area = 0

        def dfs(r: int, c: int) -> None:
            nonlocal current_area
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return
            grid[r][c] = 0
            current_area += 1
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    current_area = 0
                    dfs(r, c)
                    if current_area > max_area:
                        max_area = current_area
        
        return max_area
