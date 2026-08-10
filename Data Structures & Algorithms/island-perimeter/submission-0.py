from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        perimeter = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    perimeter += 4
                    if r - 1 >= 0 and grid[r - 1][c]:
                        perimeter -= 1
                    if r + 1 < m and grid[r + 1][c]:
                        perimeter -= 1
                    if c - 1 >= 0 and grid[r][c - 1]:
                        perimeter -= 1
                    if c + 1 < n and grid[r][c + 1]:
                        perimeter -= 1
        return perimeter
